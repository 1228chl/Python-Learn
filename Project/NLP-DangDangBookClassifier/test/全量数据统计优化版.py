import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tqdm import tqdm  # 务必安装：pip install tqdm
from config.config import Config

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

config = Config()
tokenizer = config.bert_tokenizer


def analyze_text_length(file_path, dataset_name, sample_ratio=0.15):
    """
    分析单个数据集的文本长度分布（支持采样 + 批处理编码）
    """
    if not os.path.exists(file_path):
        print(f"⚠️ 文件不存在: {file_path}")
        return None, None

    # 读取数据
    df = pd.read_csv(file_path, sep='\t')

    # 【关键优化 1】如果数据量巨大，先随机采样
    if len(df) > 50000 and sample_ratio < 1.0:
        df = df.sample(frac=sample_ratio, random_state=42)
        print(f"  📌 {dataset_name} 采样 {sample_ratio * 100:.0f}% 数据 ({len(df)} 条)")

    texts = df['text'].astype(str).tolist()

    # 【关键优化 2】批处理编码（不再用 for 循环单条调用）
    print(f"  🔄 正在进行批量分词编码（批处理加速）...")
    encodings = tokenizer(
        texts,
        add_special_tokens=True,
        truncation=False,  # 不截断，统计真实长度
        padding=False,  # 不填充，节省内存
        return_attention_mask=False  # 不需要掩码，节省内存
    )

    # 提取长度
    lengths = [len(ids) for ids in encodings['input_ids']]
    lengths = np.array(lengths)

    # 统计指标
    stats = {
        '数据集': dataset_name,
        '样本数(抽样后)': len(lengths),
        '平均长度': np.mean(lengths),
        '中位数': np.median(lengths),
        'P75': np.percentile(lengths, 75),
        'P90': np.percentile(lengths, 90),
        'P95': np.percentile(lengths, 95),  # 核心参考值
        'P99': np.percentile(lengths, 99),
        '最大值': np.max(lengths),
    }
    return stats, lengths


def plot_distribution(lengths_dict, save_path=None):
    """绘制分布图"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    data_for_box = [lengths for lengths in lengths_dict.values() if lengths is not None]
    labels = [name for name in lengths_dict.keys() if lengths_dict[name] is not None]

    # 箱线图
    axes[0].boxplot(data_for_box, labels=labels, patch_artist=True, showmeans=True)
    axes[0].set_title('文本长度箱线图', fontsize=14)
    axes[0].set_ylabel('Token 数量')
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # 核密度图
    for name, lengths in lengths_dict.items():
        if lengths is not None:
            sns.kdeplot(lengths, label=name, ax=axes[1], linewidth=2)
    axes[1].set_title('文本长度核密度分布', fontsize=14)
    axes[1].set_xlabel('Token 数量')
    axes[1].legend()
    axes[1].grid(linestyle='--', alpha=0.7)

    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"\n📊 图表已保存至: {save_path}")
    plt.show()


if __name__ == "__main__":
    print("🚀 开始分析全量数据长度分布（批处理加速 + 智能采样）...\n")

    datasets = {
        '训练集': config.train_path,
        '验证集': config.dev_path,
        '测试集': config.test_path,
    }

    all_stats = []
    lengths_collection = {}

    for name, path in datasets.items():
        print(f"⏳ 正在处理 {name} ...")
        stats, lengths = analyze_text_length(path, name, sample_ratio=0.15)  # 只抽 15%
        if stats:
            all_stats.append(stats)
            lengths_collection[name] = lengths
            print(f"   ✅ 完成，抽样后样本数: {stats['样本数(抽样后)']}")

    # 打印统计表格
    print("\n" + "=" * 80)
    print("📋 文本长度统计汇总 (基于抽样 15%，单位: Token)")
    print("=" * 80)
    df_stats = pd.DataFrame(all_stats)
    pd.set_option('display.float_format', '{:.2f}'.format)
    print(df_stats.to_string(index=False))

    # 给出建议
    print("\n" + "=" * 80)
    print("💡 超参数 max_len 设置建议")
    print("=" * 80)

    train_row = df_stats[df_stats['数据集'] == '训练集']
    if not train_row.empty:
        p95 = train_row['P95'].values[0]
        p99 = train_row['P99'].values[0]
        old_len = config.max_len

        suggested = int(np.ceil(p95 / 32) * 32)

        print(f"当前 config 中的 max_len = {old_len}")
        print(f"训练集 P95 分位数 = {p95:.2f} (覆盖 95% 的抽样样本)")
        print(f"\n✨ 建议将 max_len 设为: {suggested}")
        print(f"   (若显存充足，可设为: {int(np.ceil(p99 / 32) * 32)} 以覆盖 99%)")
        print(f"\n📌 显存变化: max_len {old_len} -> {suggested}，约增加 {(suggested / old_len - 1) * 100:.1f}% 占用")

    # 画图
    plot_distribution(lengths_collection,
                      save_path=os.path.join(config.root_path, 'data/processed/length_distribution.png'))