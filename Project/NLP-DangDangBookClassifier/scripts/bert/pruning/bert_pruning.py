import os
import torch
import torch.nn.utils.prune as prune
import pandas as pd
import time
import random
from torch.utils.data import DataLoader, Dataset
from transformers import BertForSequenceClassification
from sklearn.metrics import accuracy_score, f1_score
from config.config import Config

# -------------------- 数据集类（复用） --------------------
class BertDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_len, sample_frac=1.0):
        self.data = pd.read_csv(file_path, sep='\t')
        if sample_frac < 1.0:
            self.data = self.data.sample(frac=sample_frac, random_state=42)
        self.texts = self.data['text'].astype(str).values
        self.labels = self.data['label'].values
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding='max_length',
            max_length=self.max_len,
            return_tensors='pt'
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'label': torch.tensor(label, dtype=torch.long)
        }

# -------------------- 评估函数 --------------------
def evaluate(model, dataloader, device='cpu'):
    model.eval()
    model.to(device)
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            preds = torch.argmax(logits, dim=1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    acc = accuracy_score(all_labels, all_preds)
    f1 = f1_score(all_labels, all_preds, average='macro')
    return acc, f1

# -------------------- 稀疏度统计 --------------------
def show_model_sparse(model):
    """统计模型中所有 Linear 层权重的稀疏度（零占比）"""
    zero_total = 0
    total = 0
    for name, param in model.named_parameters():
        if 'weight' in name and 'layer' in name:  # 只统计编码器层
            zero_total += torch.sum(param == 0).item()
            total += param.numel()
    return zero_total / total if total > 0 else 0

# -------------------- 主函数 --------------------
def main():
    config = Config()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 1. 加载微调模型（CPU 上剪枝更稳定）
    print(f"从 {config.bert_model_path} 加载模型...")
    model = BertForSequenceClassification.from_pretrained(config.bert_model_path)
    model.eval()

    # 2. 准备训练/验证数据（只用少量样本评估）
    tokenizer = config.bert_tokenizer
    # 从验证集随机取 500 条作为评估集
    eval_dataset = BertDataset(config.dev_path, tokenizer, config.max_len, sample_frac=0.01)  # 约 800 条
    eval_loader = DataLoader(eval_dataset, batch_size=config.batch_size, shuffle=False)

    # 3. 剪枝前评估
    print("\n=== 剪枝前模型性能 ===")
    acc_before, f1_before = evaluate(model, eval_loader, device='cpu')
    print(f"准确率: {acc_before:.4f}, F1: {f1_before:.4f}")
    sparse_before = show_model_sparse(model)
    print(f"权重稀疏度: {sparse_before:.2%}")

    # 4. 执行全局非结构化剪枝（剪枝比例 20%）
    pruning_ratio = 0.2  # 可调
    print(f"\n开始全局剪枝 (比例: {pruning_ratio*100}%)...")

    # 获取所有编码器层中的 Linear 权重（query, key, value, output, intermediate, etc.）
    parameters_to_prune = []
    for layer in model.bert.encoder.layer:
        # 剪枝 attention 和 FFN 的线性层
        for module in [layer.attention.self.query,
                       layer.attention.self.key,
                       layer.attention.self.value,
                       layer.attention.output.dense,
                       layer.intermediate.dense,
                       layer.output.dense]:
            parameters_to_prune.append((module, 'weight'))

    # 全局剪枝
    prune.global_unstructured(
        parameters_to_prune,
        pruning_method=prune.L1Unstructured,
        amount=pruning_ratio,
    )

    # 移除剪枝掩码（固化剪枝，即永久将权重置零）
    for module, param_name in parameters_to_prune:
        prune.remove(module, param_name)

    print("剪枝完成！")

    # 5. 剪枝后评估
    print("\n=== 剪枝后模型性能 ===")
    acc_after, f1_after = evaluate(model, eval_loader, device='cpu')
    print(f"准确率: {acc_after:.4f}, F1: {f1_after:.4f}")
    sparse_after = show_model_sparse(model)
    print(f"权重稀疏度: {sparse_after:.2%}")

    # 6. 保存剪枝模型
    os.makedirs(config.pruning_dir, exist_ok=True)
    model.save_pretrained(config.pruning_dir)
    tokenizer.save_pretrained(config.pruning_dir)
    print(f"\n✅ 剪枝模型已保存至: {config.pruning_dir}")

    # 7. 速度对比（可选）
    print("\n=== CPU 推理速度对比 (100次) ===")
    dummy_input = {
        'input_ids': torch.randint(0, 10000, (1, config.max_len)),
        'attention_mask': torch.ones((1, config.max_len)),
    }
    # 重新加载原始模型（避免与剪枝模型共享内存）
    model_orig = BertForSequenceClassification.from_pretrained(config.bert_model_path).to('cpu')
    model_pruned = model.to('cpu')

    start = time.time()
    with torch.no_grad():
        for _ in range(100):
            _ = model_orig(**dummy_input)
    t_orig = time.time() - start

    start = time.time()
    with torch.no_grad():
        for _ in range(100):
            _ = model_pruned(**dummy_input)
    t_pruned = time.time() - start

    print(f"原始模型: {t_orig:.4f}s")
    print(f"剪枝模型: {t_pruned:.4f}s")
    print(f"加速比: {t_orig / t_pruned:.2f}x")

    # 8. 说明
    print("\n⚠️ 注意: 非结构化剪枝带来的零权重不会自动加速原始 PyTorch 推理。")
    print("   若要真正加速，请考虑使用 torch.sparse 或导出为 ONNX + OpenVINO 等支持稀疏运算的框架。")
    print("   此外，剪枝后建议进行 1~2 个 epoch 的微调以恢复精度。")

if __name__ == "__main__":
    main()