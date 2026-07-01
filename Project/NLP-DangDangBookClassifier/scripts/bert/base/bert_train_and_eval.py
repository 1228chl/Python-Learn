import os
import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import BertForSequenceClassification, BertTokenizer, get_linear_schedule_with_warmup
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
from tqdm import tqdm
import time
import logging
from config.config import Config

# -------------------- 日志配置 --------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------- 全局变量（用于 worker 进程） --------------------
_worker_tokenizer = None
_worker_max_len = None
config = Config()

def worker_init_fn(worker_id):
    """在每个 worker 进程中初始化 tokenizer"""
    global _worker_tokenizer, _worker_max_len
    # 注意：这里要使用 Config 中的路径，但我们不能传递 Config 对象
    # 因此从 Config 中读取路径并硬编码，或从环境变量获取，或使用全局变量
    # 更健壮的做法：从 config 读取，但 config 可能不可 pickle，所以我们直接从模块导入 config
    # 但导入 config 也会加载 BertModel，但我们只需要 tokenizer，所以可以只加载 tokenizer
    # 我们可以在主进程中把 tokenizer 路径和 max_len 作为全局变量设置
    # 但更好的方式：在 worker_init_fn 中重新加载 tokenizer
    if _worker_tokenizer is None:
        # 从 Config 中获取路径（但 Config 不可 pickle，所以我们可以直接使用字符串）
        # 这里假设 config 已经在模块级别被实例化，但为了安全，我们直接硬编码路径或从环境变量获取
        # 推荐在模块级别定义常量
        _worker_tokenizer = BertTokenizer.from_pretrained(config.bert_base_chinese_path)
        # max_len 也从全局获取
        _worker_max_len = 32   # 或从 config 获取，但 config 不可 pickle，所以我们从主进程传递过来
        # 我们可以通过设置全局变量来传递 max_len
        # 见后面的 setup_worker_globals 函数

def setup_worker_globals(max_len, tokenizer_path):
    """在主进程中设置全局变量，供 worker 使用"""
    global _worker_max_len, _worker_tokenizer_path
    _worker_max_len = max_len
    _worker_tokenizer_path = tokenizer_path

# -------------------- 数据集类（可 pickle） --------------------
class BertDataset(Dataset):
    def __init__(self, file_path, max_len):
        self.data = pd.read_csv(file_path, sep='\t')
        self.texts = self.data['text'].astype(str).values
        self.labels = self.data['label'].values
        self.max_len = max_len  # 存储 max_len，用于 tokenization

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        # 使用全局 tokenizer 进行编码
        # 注意：tokenizer 必须在 worker 中已被初始化
        tokenizer = _worker_tokenizer
        if tokenizer is None:
            raise RuntimeError("Tokenizer not initialized in worker. Make sure worker_init_fn is called.")
        encoding = tokenizer(
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
def evaluate(model, dataloader, device):
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in tqdm(dataloader, desc='Evaluating'):
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

# -------------------- Checkpoint 函数 --------------------
def save_checkpoint(state, filename):
    torch.save(state, filename)
    logger.info(f"Checkpoint 已保存至: {filename}")

def load_checkpoint(filename, model, optimizer, scheduler, scaler, device,config):
    if os.path.exists(filename):
        checkpoint = torch.load(filename, map_location=device)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
        if scaler and 'scaler_state_dict' in checkpoint and checkpoint['scaler_state_dict'] is not None:
            scaler.load_state_dict(checkpoint['scaler_state_dict'])
        start_epoch = checkpoint['epoch'] + 1
        start_batch = checkpoint['batch'] + 1
        best_metric = checkpoint['best_metric']
        patience_counter = checkpoint['patience_counter']
        logger.info(f"恢复训练: 从 Epoch {start_epoch}, Batch {start_batch}, 当前最佳 {config.best_metric}={best_metric:.4f}")
        return start_epoch, start_batch, best_metric, patience_counter
    else:
        logger.info("未找到 Checkpoint，从头开始训练")
        return 1, 1, -float('inf'), 0

# -------------------- 主函数 --------------------
def main():
    device = config.device

    # 调整 Dropout
    config.bert_config.hidden_dropout_prob = 0.2
    config.bert_config.attention_probs_dropout_prob = 0.2
    config.bert_config.num_labels = config.class_num

    logger.info(f"设备: {device}, 类别数: {config.class_num}")
    logger.info(f"Dropout: hidden={config.bert_config.hidden_dropout_prob}, attn={config.bert_config.attention_probs_dropout_prob}")

    # 设置 worker 全局变量（tokenizer 路径和 max_len）
    setup_worker_globals(config.max_len, config.bert_base_chinese_path)

    # 数据集（不再传入 tokenizer）
    train_dataset = BertDataset(config.train_path, config.max_len)
    dev_dataset = BertDataset(config.dev_path, config.max_len)

    # DataLoader 配置（启用多进程）
    num_workers = min(4, os.cpu_count())  # 根据 CPU 核数调整
    train_loader = DataLoader(
        train_dataset,
        batch_size=config.batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True if device.type == 'cuda' else False,
        prefetch_factor=4,
        worker_init_fn=worker_init_fn   # 关键：每个 worker 初始化 tokenizer
    )
    dev_loader = DataLoader(
        dev_dataset,
        batch_size=config.batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True if device.type == 'cuda' else False,
        prefetch_factor=4,
        worker_init_fn=worker_init_fn
    )

    # 模型
    model = BertForSequenceClassification.from_pretrained(
        config.bert_base_chinese_path,
        config=config.bert_config
    ).to(device)

    # 优化器
    optimizer = AdamW(model.parameters(), lr=config.lr)
    total_steps = len(train_loader) * config.epochs
    warmup_steps = int(0.1 * total_steps)
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
        num_training_steps=total_steps
    )

    # 混合精度（仅 CUDA）
    use_amp = (device.type == 'cuda')
    if use_amp:
        from torch.cuda.amp import autocast, GradScaler
        scaler = GradScaler()
    else:
        autocast = None
        scaler = None

    # Checkpoint 路径
    checkpoint_path = os.path.join(os.path.dirname(config.bert_model_path), 'training_checkpoint.pt')
    start_epoch, start_batch, best_metric, patience_counter = load_checkpoint(
        checkpoint_path, model, optimizer, scheduler, scaler, device,config
    )

    logger.info(f"训练样本数: {len(train_dataset)}, 验证样本数: {len(dev_dataset)}")
    logger.info(f"总步数: {total_steps}, 预热步数: {warmup_steps}")
    logger.info(f"每 {config.eval_interval} 批验证一次, 早停耐心 = {config.patience}")

    best_epoch, best_batch = -1, -1
    GRADIENT_ACCUMULATION_STEPS = getattr(config, 'gradient_accumulation_steps', 1)

    for epoch in range(start_epoch, config.epochs + 1):
        logger.info(f"\n===== Epoch {epoch}/{config.epochs} =====")
        model.train()
        total_loss = 0
        batch_cnt = 0

        start_batch_this_epoch = start_batch if epoch == start_epoch else 1

        for batch_idx, batch in enumerate(tqdm(train_loader, desc=f'Epoch {epoch} 训练'), start=1):
            if batch_idx < start_batch_this_epoch:
                continue

            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)

            if use_amp:
                with autocast():
                    outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
                    loss = outputs.loss / GRADIENT_ACCUMULATION_STEPS
                scaler.scale(loss).backward()
                if (batch_idx % GRADIENT_ACCUMULATION_STEPS == 0) or (batch_idx == len(train_loader)):
                    scaler.unscale_(optimizer)
                    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                    scaler.step(optimizer)
                    scaler.update()
                    optimizer.zero_grad()
                    scheduler.step()
            else:
                outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss / GRADIENT_ACCUMULATION_STEPS
                loss.backward()
                if (batch_idx % GRADIENT_ACCUMULATION_STEPS == 0) or (batch_idx == len(train_loader)):
                    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                    optimizer.step()
                    optimizer.zero_grad()
                    scheduler.step()

            total_loss += loss.item() * GRADIENT_ACCUMULATION_STEPS
            batch_cnt += 1

            # 验证与早停
            if batch_idx % config.eval_interval == 0 or batch_idx == len(train_loader):
                avg_loss = total_loss / batch_cnt if batch_cnt > 0 else 0
                logger.info(f"\n批 {batch_idx}/{len(train_loader)}，平均损失 {avg_loss:.4f}，开始验证...")
                dev_acc, dev_f1 = evaluate(model, dev_loader, device)
                current_metric = dev_f1 if config.best_metric == 'f1' else dev_acc
                logger.info(f"验证集 -> 准确率: {dev_acc:.4f}, F1: {dev_f1:.4f}")

                if current_metric > best_metric:
                    best_metric = current_metric
                    patience_counter = 0
                    best_epoch = epoch
                    best_batch = batch_idx

                    os.makedirs(os.path.dirname(config.bert_model_path), exist_ok=True)
                    model.save_pretrained(config.bert_model_path)
                    config.bert_tokenizer.save_pretrained(config.bert_model_path)
                    logger.info(f"✅ 新最佳模型已保存（{config.best_metric}: {best_metric:.4f}）")
                else:
                    patience_counter += 1
                    logger.info(f"性能未提升，早停计数: {patience_counter}/{config.patience}")

                # 保存 Checkpoint
                checkpoint_state = {
                    'epoch': epoch,
                    'batch': batch_idx,
                    'model_state_dict': model.state_dict(),
                    'optimizer_state_dict': optimizer.state_dict(),
                    'scheduler_state_dict': scheduler.state_dict(),
                    'scaler_state_dict': scaler.state_dict() if scaler else None,
                    'best_metric': best_metric,
                    'patience_counter': patience_counter,
                }
                save_checkpoint(checkpoint_state, checkpoint_path)

                if patience_counter >= config.patience:
                    logger.info("⚠️ 早停触发！停止训练。")
                    break

                total_loss = 0
                batch_cnt = 0
                model.train()

        # 重置 start_batch 以便下一 epoch 从头开始
        start_batch = 1
        if patience_counter >= config.patience:
            break

    logger.info(f"\n🎉 训练完成！最佳 {config.best_metric}: {best_metric:.4f} (Epoch {best_epoch}, Batch {best_batch})")
    logger.info(f"最佳模型保存在: {config.bert_model_path}")

if __name__ == "__main__":
    main()