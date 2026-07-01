import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from config.config import Config

# 设置中文字体，防止图表乱码
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 加载配置（自动加载 bert tokenizer）
config = Config()
tokenizer = config.bert_tokenizer


def analyze_text_length(file_path, dataset_name, max_display_len=512):
    """
    分析单个数据集的文本长度分布
    """
    if not os.path.exists(file_path):
        print(f"⚠️ 文件不存在，跳过: {file_path}")
        return None, None

    # 读取数据（你的数据是 tab 分隔）
    df = pd.read_csv(file_path, sep='\t')
    texts = df['text'].astype(str).tolist()

    # 计算每个样本的 token 长度（不截断，真实长度）
    lengths = []
    for text in texts:
        # 这里不添加 [CLS] 和 [SEP]，只计算实际文本分词后的长度
        tokens = tokenizer.encode(text, add_special_tokens=True, truncation=False)
        lengths.append(len(tokens))

    # 转为 numpy 数组便于计算
    lengths = np.array(lengths)

    # 计算常用统计指标
    stats = {
        '数据集': dataset_name,
        '样本数': len(lengths),
        '平均长度': np.mean(lengths),
        '中位数': np.median(lengths),
        '标准差': np.std(lengths),
        '最小值': np.min(lengths),
        '最大值': np.max(lengths),
        'P75 (75%)': np.percentile(lengths, 75),
        'P90 (90%)': np.percentile(lengths, 90),
        'P95 (95%)': np.percentile(lengths, 95),  # 推荐将 max_len 设为此值附近
        'P99 (99%)': np.percentile(lengths, 99),
    }

    return stats, lengths


def plot_distribution(lengths_dict, save_path=None):
    """
    绘制多个数据集的长度分布箱线图 + 核密度图
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # 1. 箱线图 (Boxplot) - 直观查看离群点和四分位距
    data_for_box = [lengths for _, lengths in lengths_dict.items() if lengths is not None]
    labels = [name for name, lengths in lengths_dict.items() if lengths is not None]

    bp = axes[0].boxplot(data_for_box, labels=labels, patch_artist=True,
                         showmeans=True, meanline=True)
    axes[0].set_title('各数据集文本长度箱线图', fontsize=14)
    axes[0].set_ylabel('Token 数量')
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # 添加 P95 参考线（以训练集为准）
    if '训练集' in labels:
        train_idx = labels.index('训练集')
        p95_val = np.percentile(data_for_box[train_idx], 95)
        axes[0].axhline(y=p95_val, color='r', linestyle='--',
                        label=f'训练集 P95 = {int(p95_val)}')
        axes[0].legend()

    # 2. 核密度图 (KDE) - 查看整体分布形态
    for name, lengths in lengths_dict.items():
        if lengths is not None:
            sns.kdeplot(lengths, label=name, ax=axes[1], linewidth=2)
    axes[1].set_title('各数据集文本长度核密度分布', fontsize=14)
    axes[1].set_xlabel('Token 数量')
    axes[1].legend()
    axes[1].grid(linestyle='--', alpha=0.7)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)
        print(f"\n📊 图表已保存至: {save_path}")

    plt.show()


if __name__ == "__main__":
    print("🚀 开始分析全量数据长度分布...\n")

    # 定义需要分析的数据集路径
    datasets = {
        '训练集': config.train_path,
        '验证集': config.dev_path,
        '测试集': config.test_path,
    }

    all_stats = []
    lengths_collection = {}

    for name, path in datasets.items():
        stats, lengths = analyze_text_length(path, name)
        if stats:
            all_stats.append(stats)
            lengths_collection[name] = lengths
            print(f"✅ {name} 分析完成，样本数: {stats['样本数']}")

    # 打印统计表格
    print("\n" + "=" * 80)
    print("📋 全量数据长度统计汇总 (单位: Token，已包含 [CLS] 和 [SEP])")
    print("=" * 80)

    df_stats = pd.DataFrame(all_stats)
    # 设置显示精度
    pd.set_option('display.float_format', '{:.2f}'.format)
    print(df_stats.to_string(index=False))

    # 给出建议
    print("\n" + "=" * 80)
    print("💡 超参数 max_len 设置建议")
    print("=" * 80)

    train_row = df_stats[df_stats['数据集'] == '训练集']
    if not train_row.empty:
        p95 = train_row['P95 (95%)'].values[0]
        p99 = train_row['P99 (99%)'].values[0]
        max_len_old = config.max_len

        # 建议值：取 P95 并向上取整到 32 的倍数（BERT 效率较高）
        suggested = int(np.ceil(p95 / 32) * 32)

        print(f"当前 config 中的 max_len = {max_len_old}")
        print(f"训练集 P95 分位数 = {p95:.2f} (覆盖 95% 的样本)")
        print(f"训练集 P99 分位数 = {p99:.2f} (覆盖 99% 的样本)")
        print(f"\n✨ 建议将 max_len 设为: {suggested} (基于 P95)")
        print(f"   (如果想覆盖更全，可设为: {int(np.ceil(p99 / 32) * 32)})")

        # 估算显存影响
        print(f"\n📌 显存影响提醒: max_len 从 {max_len_old} -> {suggested}")
        print(f"   大约增加 {(suggested / max_len_old - 1) * 100 :.1f}% 显存占用")

    # 画图
    plot_distribution(lengths_collection,
                      save_path=os.path.join(config.root_path, 'data/processed/length_distribution.png'))