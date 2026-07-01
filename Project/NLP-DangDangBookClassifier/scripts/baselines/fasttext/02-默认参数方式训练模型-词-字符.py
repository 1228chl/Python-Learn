import fasttext
import time
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,classification_report
from config.config import Config

# 加载配置
config = Config()

# 构建 类别名 → 数字 的映射（用于评估时转换）
class2id = config.class2id

def train_and_evaluate(train_file, dev_file, test_file, model_save_path, label_map, model_name=""):
    """
    使用默认参数训练 FastText 模型，并评估验证集和测试集
    """
    print(f"\n{'='*50}")
    print(f"开始训练 {model_name} FastText 模型")
    print(f"训练文件: {train_file}")
    print(f"模型保存至: {model_save_path}")

    # 1. 训练（使用默认参数，仅设置 epoch=5 和 wordNgrams=1，这些就是默认值）
    start_time = time.time()
    model = fasttext.train_supervised(
        input=train_file,
        epoch=25,         # 从 5 提升到 25
        lr=0.1,           # 默认值
        wordNgrams=2,     # 从 1 提升到 2（捕捉短语）
        dim=200,          # 从 100 提升到 200
        loss='softmax',   # 默认值
        minCount=2,       # 过滤低频词
        bucket=2000000,   # 默认值
        verbose=2
    )
    train_time = time.time() - start_time
    print(f"训练完成，耗时 {train_time:.2f} 秒")

    # 保存模型
    model.save_model(model_save_path)
    print(f"模型已保存至 {model_save_path}")

    # 2. 评估函数：读取 FastText 格式文件，预测并计算指标
    def evaluate(data_file, dataset_name=""):
        # 读取 FastText 格式文件
        with open(data_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        y_true = []
        y_pred = []
        for line in lines:
            # 解析真实标签
            parts = line.strip().split(' ', 1)
            if len(parts) != 2:
                continue
            label_part = parts[0]          # 例如 "__label__童书"
            text = parts[1]                # 文本内容
            true_label_name = label_part.replace('__label__', '')
            true_label_id = label_map[true_label_name]
            y_true.append(true_label_id)

            # 预测
            pred_result = model.predict([text], k=1)  # 返回 (labels, probabilities)
            pred_label_name = pred_result[0][0][0].replace('__label__', '')
            pred_label_id = label_map[pred_label_name]
            y_pred.append(pred_label_id)

        # 计算指标
        acc = accuracy_score(y_true, y_pred)
        prec = precision_score(y_true, y_pred, average='macro', zero_division=0)
        rec = recall_score(y_true, y_pred, average='macro', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)

        print(f"\n【{dataset_name} 评估结果】")
        print(f"准确率 (Accuracy): {acc*100:.2f}%")
        print(f"宏平均精确率 (Macro Precision): {prec*100:.2f}%")
        print(f"宏平均召回率 (Macro Recall): {rec*100:.2f}%")
        print(f"宏平均 F1 (Macro F1): {f1*100:.2f}%")
        print(classification_report(y_true, y_pred, target_names=list(class2id.keys()), digits=4))

        # 可选：打印详细分类报告（如果类别不太多，可以启用）
        # print(classification_report(y_true, y_pred, target_names=list(label_map.keys()), zero_division=0))

        return acc, prec, rec, f1

    # 评估验证集
    evaluate(dev_file, dataset_name="验证集")

    # 评估测试集
    evaluate(test_file, dataset_name="测试集")

    return model

if __name__ == "__main__":
    # ----- 词级训练 -----
    train_and_evaluate(
        train_file=config.process_train_path_words,
        dev_file=config.process_dev_path_words,
        test_file=config.process_test_path_words,
        model_save_path=config.ft_word_default_model_path,
        label_map=class2id,
        model_name="词级"
    )

    # ----- 字符级训练 -----
    train_and_evaluate(
        train_file=config.process_train_path_chars,
        dev_file=config.process_dev_path_chars,
        test_file=config.process_test_path_chars,
        model_save_path=config.ft_char_default_model_path,
        label_map=class2id,
        model_name="字符级"
    )

    print("\n所有训练和评估完成！")