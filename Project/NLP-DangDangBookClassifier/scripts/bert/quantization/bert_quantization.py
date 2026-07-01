import os
import sys
import torch
from torch.quantization import quantize_dynamic
from transformers import BertForSequenceClassification, BertTokenizer
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
import time
from config.config import Config

# -------------------- 本地数据集类（避免导入问题） --------------------
class BertDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_len):
        self.data = pd.read_csv(file_path, sep='\t')
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

# -------------------- 主函数 --------------------
def main():
    config = Config()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 1. 加载微调后的最佳模型
    print(f"正在从 {config.bert_model_path} 加载模型...")
    model = BertForSequenceClassification.from_pretrained(config.bert_model_path)
    model.eval()

    # 2. 创建输出目录
    os.makedirs(config.quantization_dir, exist_ok=True)

    # 3. 动态量化（仅量化 Linear 层）
    print("正在进行动态量化...")
    quantized_model = quantize_dynamic(
        model,
        {torch.nn.Linear},
        dtype=torch.qint8
    )
    print("✅ 量化完成！")

    # 4. 保存量化模型
    quantized_state_path = config.quantization_dir + 'quantized_model.pth'
    torch.save(quantized_model.state_dict(), quantized_state_path)
    quantized_model.config.save_pretrained(config.quantization_dir)
    print(f"量化模型保存至: {quantized_state_path}")
    print(f"模型配置保存至: {config.quantization_dir}")

    # 5. 性能对比（CPU）
    print("\n=== 性能对比 (CPU) ===")
    dummy_input = {
        'input_ids': torch.randint(0, 10000, (1, config.max_len)),
        'attention_mask': torch.ones((1, config.max_len)),
    }

    model_cpu = model.to('cpu')
    quantized_model_cpu = quantized_model.to('cpu')

    with torch.no_grad():
        start = time.time()
        for _ in range(100):
            _ = model_cpu(**dummy_input)
        orig_time = time.time() - start
    print(f"原始 FP32 模型推理 100 次耗时: {orig_time:.4f} s")

    with torch.no_grad():
        start = time.time()
        for _ in range(100):
            _ = quantized_model_cpu(**dummy_input)
        quant_time = time.time() - start
    print(f"量化 INT8 模型推理 100 次耗时: {quant_time:.4f} s")
    print(f"🚀 加速比: {orig_time / quant_time:.2f}x")

    # 6. 精度对比（在验证集上）
    print("\n=== 精度对比 (验证集) ===")
    tokenizer = config.bert_tokenizer
    dev_dataset = BertDataset(config.dev_path, tokenizer, config.max_len)
    dev_dataset.data = dev_dataset.data.sample(n=100,random_state=42)
    dev_loader = DataLoader(dev_dataset, batch_size=config.batch_size, shuffle=False)

    # 原始模型
    print("原始 FP32 模型：")
    acc_fp32, f1_fp32 = evaluate(model_cpu, dev_loader, device='cpu')
    print(f"  准确率: {acc_fp32:.4f}, F1: {f1_fp32:.4f}")

    # 量化模型
    print("量化 INT8 模型：")
    acc_int8, f1_int8 = evaluate(quantized_model_cpu, dev_loader, device='cpu')
    print(f"  准确率: {acc_int8:.4f}, F1: {f1_int8:.4f}")

    print("\n✅ 量化流程全部完成！")
    print("💡 使用量化模型加载方式：")
    print(f"   model = BertForSequenceClassification.from_pretrained('{config.quantization_dir}')")
    print(f"   model.load_state_dict(torch.load('{quantized_state_path}'))")
    print("   model.eval()")

if __name__ == "__main__":
    main()