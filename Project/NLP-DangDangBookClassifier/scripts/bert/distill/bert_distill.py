import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from transformers import BertForSequenceClassification
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
from tqdm import tqdm
import time
import logging
from config.config import Config

# -------------------- 日志配置 --------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------- 1. 定义 BiLSTM 学生模型 --------------------
class BiLSTMStudent(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_layers, num_labels, dropout=0.3):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(
            embed_dim,
            hidden_dim,
            num_layers,
            batch_first=True,
            bidirectional=True,
            dropout=dropout if num_layers > 1 else 0
        )
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(hidden_dim * 2, num_labels)  # 双向所以 *2

    def forward(self, input_ids, attention_mask=None):
        # 1. 嵌入
        embedded = self.embedding(input_ids)  # (batch, seq, embed_dim)

        # 2. LSTM 编码
        lstm_out, _ = self.lstm(embedded)  # (batch, seq, hidden_dim*2)

        # 3. 池化：使用 attention_mask 进行均值池化（忽略 padding 部分）
        if attention_mask is not None:
            mask = attention_mask.unsqueeze(-1).float()
            pooled = torch.sum(lstm_out * mask, dim=1) / torch.sum(mask, dim=1)
        else:
            pooled = torch.mean(lstm_out, dim=1)

        # 4. 分类
        pooled = self.dropout(pooled)
        logits = self.classifier(pooled)
        return logits

# -------------------- 2. 数据集类（复用） --------------------
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

# -------------------- 3. 评估函数 --------------------
def evaluate(model, dataloader, device):
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in tqdm(dataloader, desc='Evaluating'):
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits if hasattr(outputs,'logits') else outputs
            preds = torch.argmax(logits, dim=1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    acc = accuracy_score(all_labels, all_preds)
    f1 = f1_score(all_labels, all_preds, average='macro')
    return acc, f1

# -------------------- 4. 蒸馏损失函数 --------------------
def distillation_loss(student_logits, teacher_logits, labels, temperature=4.0, alpha=0.7):
    # 软标签损失（KL散度）
    soft_loss = F.kl_div(
        F.log_softmax(student_logits / temperature, dim=-1),
        F.softmax(teacher_logits / temperature, dim=-1),
        reduction='batchmean'
    ) * (temperature ** 2)
    # 硬标签损失（交叉熵）
    hard_loss = F.cross_entropy(student_logits, labels)
    return alpha * soft_loss + (1 - alpha) * hard_loss

# -------------------- 5. 主函数 --------------------
def main():
    config = Config()
    device = config.device
    logger.info(f"设备: {device}")

    # 5.1 加载教师模型（你微调好的 BERT）
    logger.info(f"正在加载教师模型: {config.bert_model_path}")
    teacher = BertForSequenceClassification.from_pretrained(config.bert_model_path).to(device)
    teacher.eval()  # 冻结教师
    logger.info("教师模型加载完成！")

    # 5.2 创建 BiLSTM 学生模型
    vocab_size = len(config.bert_tokenizer)  # BERT 词表大小
    logger.info(f"词表大小: {vocab_size}，正在创建 BiLSTM 学生模型...")
    student = BiLSTMStudent(
        vocab_size=vocab_size,
        embed_dim=256,          # 嵌入维度
        hidden_dim=256,         # LSTM 隐藏层维度
        num_layers=2,           # LSTM 层数
        num_labels=config.class_num,
        dropout=0.3
    ).to(device)
    logger.info(f"学生模型参数量: {sum(p.numel() for p in student.parameters()):,}")

    # 5.3 准备数据（蒸馏通常使用训练集，但可以用验证集做评估）
    tokenizer = config.bert_tokenizer
    logger.info("正在加载训练数据...")
    train_dataset = BertDataset(config.train_path, tokenizer, config.max_len)
    # 采样 10% 数据以加速演示（实际蒸馏可用全量）
    # train_dataset.data = train_dataset.data.sample(frac=0.1, random_state=42)
    train_loader = DataLoader(
        train_dataset,
        batch_size=config.batch_size,
        shuffle=True,
        num_workers=4,
        pin_memory=True if device.type == 'cuda' else False
    )

    # 验证集（用于评估蒸馏效果）
    dev_dataset = BertDataset(config.dev_path, tokenizer, config.max_len)
    dev_loader = DataLoader(
        dev_dataset,
        batch_size=config.batch_size,
        shuffle=False,
        num_workers=4,
        pin_memory=True if device.type == 'cuda' else False
    )

    # 5.4 优化器与调度器
    optimizer = torch.optim.AdamW(student.parameters(), lr=2e-4)
    total_steps = len(train_loader)  # 蒸馏 3 个 epoch
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=total_steps)

    # 5.5 蒸馏训练
    logger.info(f"开始蒸馏训练，共 {len(train_loader)} 个 batch，3 个 Epoch")
    best_f1 = 0.0
    distill_dir = config.distill_dir

    for epoch in range(1, 4):
        student.train()
        total_loss = 0
        progress_bar = tqdm(train_loader, desc=f'Epoch {epoch}/3')
        start_time = time.time()

        for batch in progress_bar:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)

            # 教师推理（无梯度）
            with torch.no_grad():
                teacher_outputs = teacher(input_ids, attention_mask=attention_mask)
                teacher_logits = teacher_outputs.logits

            # 学生推理
            student_logits = student(input_ids, attention_mask=attention_mask)

            # 计算蒸馏损失
            loss = distillation_loss(student_logits, teacher_logits, labels)

            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(student.parameters(), max_norm=1.0)
            optimizer.step()
            scheduler.step()

            total_loss += loss.item()
            progress_bar.set_postfix({'loss': f'{loss.item():.4f}'})

        avg_loss = total_loss / len(train_loader)
        logger.info(f"Epoch {epoch} 完成，平均损失: {avg_loss:.4f}，耗时: {time.time()-start_time:.2f}s")

        # 每个 epoch 结束后在验证集上评估
        logger.info("正在验证学生模型...")
        acc, f1 = evaluate(student, dev_loader, device)
        logger.info(f"验证集 -> 准确率: {acc:.4f}, F1: {f1:.4f}")

        # 保存最佳模型
        if f1 > best_f1:
            best_f1 = f1
            os.makedirs(distill_dir, exist_ok=True)
            torch.save(student.state_dict(), os.path.join(distill_dir, 'best_model.pth'))
            # 保存配置信息（方便加载）
            torch.save({
                'vocab_size': vocab_size,
                'embed_dim': 256,
                'hidden_dim': 256,
                'num_layers': 2,
                'num_labels': config.class_num,
                'dropout': 0.3,
            }, os.path.join(distill_dir, 'config.pth'))
            logger.info(f"✅ 新最佳学生模型已保存 (F1: {best_f1:.4f})")

    logger.info(f"\n🎉 蒸馏完成！最佳 F1: {best_f1:.4f}")
    logger.info(f"学生模型保存在: {distill_dir}")

    # 额外：对比教师模型在验证集上的表现
    logger.info("\n=== 教师模型在验证集上的基准 ===")
    acc_t, f1_t = evaluate(teacher, dev_loader, device)
    logger.info(f"教师 BERT 准确率: {acc_t:.4f}, F1: {f1_t:.4f}")

if __name__ == "__main__":
    main()