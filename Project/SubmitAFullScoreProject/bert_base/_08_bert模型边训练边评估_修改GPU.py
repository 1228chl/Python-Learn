# -*- coding: utf-8 -*-
"""
BERT 文本分类微调脚本（工业级修复版）
功能：训练 + 每100批验证 + 保存最佳模型 + 记录超参数
"""
from _03_bert_classifier_model import MyBertClassifier
from _01_config import Config
from _02_dataloader_utils import build_all_dataloader
import torch
import torch.nn.utils as clip_grad
from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json

# 加载配置
config = Config()
device = config.device  # 获取GPU/CPU


def print_config():
    """打印当前运行的所有超参数配置"""
    print("\n" + "=" * 60)
    print("🚀 当前训练超参数配置:")
    print(f"  Epochs          : {config.epochs}")
    print(f"  Batch Size      : {config.batch_size}")
    print(f"  Learning Rate   : {config.lr}")
    print(f"  Max Length      : {config.max_len}")
    print(f"  Class Num       : {config.class_num}")
    print(f"  Device          : {device}")
    print(f"  Optimizer       : AdamW (betas=(0.9, 0.999))")
    print(f"  Gradient Clipping: max_norm=1.0")
    print(f"  Model Save Path : {config.bert_classifier_model_save_path}")
    print("=" * 60 + "\n")


def evaluate(model, dataloader, desc="验证中"):
    """
    在给定的数据加载器上评估模型，返回各项指标
    """
    model.eval()  # 切换为评估模式（关闭Dropout）
    all_true, all_pred = [], []

    with torch.no_grad():
        for batch_texts_tensor, batch_labels_tensor in tqdm(dataloader, desc=desc):
            batch_texts_tensor = batch_texts_tensor.to(device)
            batch_labels_tensor = batch_labels_tensor.to(device)

            logits = model(batch_texts_tensor)
            preds = torch.argmax(logits, dim=1)

            all_true.extend(batch_labels_tensor.cpu().tolist())
            all_pred.extend(preds.cpu().tolist())

    # 计算全量指标
    acc = accuracy_score(all_true, all_pred)
    pre = precision_score(all_true, all_pred, average='macro', zero_division=0)
    rec = recall_score(all_true, all_pred, average='macro', zero_division=0)
    f1 = f1_score(all_true, all_pred, average='macro', zero_division=0)

    return acc, pre, rec, f1


def model_train():
    """主训练函数"""
    # 打印配置
    print_config()

    # 1. 准备数据
    train_dataloader, dev_dataloader, test_dataloader = build_all_dataloader()

    # 2. 准备模型 (送入设备)
    my_bert_model = MyBertClassifier().to(device)

    # 3. 准备损失函数和优化器
    loss_fn = torch.nn.CrossEntropyLoss(reduction='mean')
    optimizer = torch.optim.AdamW(my_bert_model.parameters(), lr=config.lr, betas=(0.9, 0.999))

    # 4. 初始化最佳分数追踪器
    best_f1 = 0.0

    # 外层循环控制轮次
    for epoch in range(1, config.epochs + 1):
        # -------------------- 训练阶段 --------------------
        my_bert_model.train()  # 开启训练模式
        total_loss, batch_cnt = 0, 0
        all_pred_labels, all_true_labels = [], []

        # 获取训练集总批次数
        total_train_batches = len(train_dataloader)

        # 内层循环
        for index, (batch_texts_tensor, batch_labels_tensor) in enumerate(
                tqdm(train_dataloader, desc=f"Epoch {epoch} 训练"), start=1):

            # 数据送入设备
            batch_texts_tensor = batch_texts_tensor.to(device)
            batch_labels_tensor = batch_labels_tensor.to(device)

            # 前向传播
            logits = my_bert_model(batch_texts_tensor)
            loss = loss_fn(logits, batch_labels_tensor)

            # 反向传播
            optimizer.zero_grad()
            loss.backward()

            # 梯度裁剪
            clip_grad.clip_grad_norm_(my_bert_model.parameters(), max_norm=1.0)

            optimizer.step()

            # 日志收集（用于每10批打印）
            total_loss += loss.item()
            batch_cnt += 1
            all_true_labels.extend(batch_labels_tensor.cpu().tolist())
            batch_pred_labels = torch.argmax(logits, dim=1)
            all_pred_labels.extend(batch_pred_labels.cpu().tolist())

            # -------------------- 每10批打印滑动窗口指标 (保留原功能) --------------------
            if index % 10 == 0 or index == total_train_batches:
                acc = accuracy_score(all_true_labels, all_pred_labels)
                pre = precision_score(all_true_labels, all_pred_labels, average='macro', zero_division=0)
                rec = recall_score(all_true_labels, all_pred_labels, average='macro', zero_division=0)
                f1 = f1_score(all_true_labels, all_pred_labels, average='macro', zero_division=0)
                avg_loss = total_loss / batch_cnt
                print(
                    f"轮次:{epoch}, 批次:{index}/{total_train_batches}, 损失:{avg_loss:.4f}, 准确率:{acc:.4f}, F1:{f1:.4f}")

                # 清空窗口统计
                total_loss, batch_cnt = 0, 0
                all_true_labels, all_pred_labels = [], []

            # -------------------- 【核心改动】每100批进行验证集评估 --------------------
            if index % 200 == 0 or index == total_train_batches:
                print(f"\n===== 在批次 {index}/{total_train_batches} 触发验证集评估 =====")

                # 调用评估函数
                dev_acc, dev_pre, dev_rec, dev_f1 = evaluate(
                    my_bert_model,
                    dev_dataloader,
                    desc=f"Epoch {epoch} 批次{index} 验证"
                )
                print(f"验证集结果 -> 准确率:{dev_acc:.4f}, 精确率:{dev_pre:.4f}, 召回率:{dev_rec:.4f}, F1:{dev_f1:.4f}")

                # 保存最佳模型及超参数
                if dev_f1 > best_f1:
                    best_f1 = dev_f1

                    # 1. 保存模型权重
                    torch.save(my_bert_model.state_dict(), config.bert_classifier_model_save_path)

                    # 2. 打包超参数并保存为 JSON 日志文件
                    best_config_log = {
                        'best_f1': best_f1,
                        'best_epoch': epoch,
                        'best_batch': index,
                        'lr': config.lr,
                        'batch_size': config.batch_size,
                        'max_len': config.max_len,
                        'hidden_size': config.bert_config.hidden_size,
                        'optimizer': 'AdamW',
                        'gradient_clip_norm': 1.0,
                        'validation_frequency': '每100批',
                        'model_save_path': config.bert_classifier_model_save_path
                    }
                    json_path = config.bert_classifier_model_save_path.replace('.pt', '_best_config.json')
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(best_config_log, f, indent=4, ensure_ascii=False)

                    print(f"✅ 新最佳模型已保存，F1={best_f1:.4f}")
                    print(f"📝 对应的超参数已保存至: {json_path}")

                # 【关键】评估完毕后，切回训练模式，继续下一批训练
                my_bert_model.train()
                print("=" * 60 + "\n")

    print(f"🎉 训练完成！最佳验证集F1为: {best_f1:.4f}")


if __name__ == '__main__':
    model_train()