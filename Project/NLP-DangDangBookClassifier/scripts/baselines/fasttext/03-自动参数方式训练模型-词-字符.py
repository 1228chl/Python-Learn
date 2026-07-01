import fasttext
import pandas as pd
import time
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from config.config import Config

# 加载配置
config = Config()

# 构建 类别名 → 数字 的映射
class2id = {v: k for k, v in config.id2class.items()}

def train_with_autotune(train_file, dev_file, test_file, model_save_path, label_map, model_name="", duration=600):
    """
    使用 FastText 自动调参训练模型
    duration: 调参时间（秒），默认 600 秒（10 分钟）
    """
    print(f"\n{'='*60}")
    print(f"开始 {model_name} FastText 自动调参训练")
    print(f"训练文件: {train_file}")
    print(f"验证文件: {dev_file}")
    print(f"调参时长: {duration} 秒")
    print(f"模型保存至: {model_save_path}")

    # 1. 自动调参训练
    start_time = time.time()
    model = fasttext.train_supervised(
        input=train_file,
        autotuneValidationFile=dev_file,   # 使用验证集调参
        autotuneDuration=duration,          # 调参时间（秒）
        # autotuneModelSize='1G',             # 限制模型大小（可选）
        verbose=2                           # 显示详细日志
    )
    train_time = time.time() - start_time
    print(f"自动调参完成，总耗时 {train_time:.2f} 秒")

    # 显示最终使用的参数
    print(f"\n✅ 自动调参选用的最佳参数:")
    print(f"   epoch: {model.epoch}")
    print(f"   lr: {model.lr}")
    print(f"   dim: {model.dim}")
    print(f"   wordNgrams: {model.wordNgrams}")
    print(f"   loss: {model.loss}")
    print(f"   minCount: {model.minCount}")
    print(f"   bucket: {model.bucket}")

    # 保存模型
    model.save_model(model_save_path)
    print(f"模型已保存至 {model_save_path}")

    # 2. 评估函数
    def evaluate(data_file, dataset_name=""):
        with open(data_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        y_true = []
        y_pred = []
        for line in lines:
            parts = line.strip().split(' ', 1)
            if len(parts) != 2:
                continue
            label_part = parts[0]
            text = parts[1]
            true_label_name = label_part.replace('__label__', '')
            true_label_id = label_map[true_label_name]
            y_true.append(true_label_id)

            pred_result = model.predict([text], k=1)
            pred_label_name = pred_result[0][0][0].replace('__label__', '')
            pred_label_id = label_map[pred_label_name]
            y_pred.append(pred_label_id)

        acc = accuracy_score(y_true, y_pred)
        prec = precision_score(y_true, y_pred, average='macro', zero_division=0)
        rec = recall_score(y_true, y_pred, average='macro', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)

        print(f"\n【{dataset_name} 自动调参结果】")
        print(f"准确率 (Accuracy): {acc*100:.2f}%")
        print(f"宏平均精确率 (Macro Precision): {prec*100:.2f}%")
        print(f"宏平均召回率 (Macro Recall): {rec*100:.2f}%")
        print(f"宏平均 F1 (Macro F1): {f1*100:.2f}%")

        return acc, prec, rec, f1

    # 评估验证集
    evaluate(dev_file, dataset_name="验证集")

    # 评估测试集
    evaluate(test_file, dataset_name="测试集")

    return model


if __name__ == "__main__":
    # 自动调参时长设置（建议 10~20 分钟）
    TUNE_DURATION = 600  # 10 分钟，可以根据需要调整

    # ----- 词级自动调参 -----
    train_with_autotune(
        train_file=config.process_train_path_words,
        dev_file=config.process_dev_path_words,
        test_file=config.process_test_path_words,
        model_save_path=config.ft_word_auto_model_path,
        label_map=class2id,
        model_name="词级",
        duration=TUNE_DURATION
    )

    # ----- 字符级自动调参 -----
    train_with_autotune(
        train_file=config.process_train_path_chars,
        dev_file=config.process_dev_path_chars,
        test_file=config.process_test_path_chars,
        model_save_path=config.ft_char_auto_model_path,
        label_map=class2id,
        model_name="字符级",
        duration=TUNE_DURATION
    )

    print("\n🎯 所有自动调参训练和评估完成！")