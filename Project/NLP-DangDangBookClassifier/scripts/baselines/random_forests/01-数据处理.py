import pandas as pd
from config.config import Config
import pandas as pd
from sklearn.model_selection import train_test_split

config = Config()

def create_fix_csv(input_path, output_path):
    # 读取全部列（不指定 usecols）
    df = pd.read_csv(input_path, encoding='utf-8')
    print(f"📋 文件 {input_path} 共有 {len(df)} 行，列名：{df.columns.tolist()}")

    # 确保有 parent_category 列
    if 'parent_category' not in df.columns:
        raise KeyError(f"文件 {input_path} 中没有 'parent_category' 列")

    # 合并小众类
    rare_categories = [
        '随堂用书', '文创', '法文原版书', '亲子共读',
        '二手书', '口袋书', '课程', '英文原版书',
        '港台书', '中小学教科书', '特装书', '老书/收藏', '诺贝尔文学奖'
    ]
    df['parent_category'] = df['parent_category'].replace(rare_categories, '其他小众书')

    print(df['parent_category'].value_counts())

    # 保存到新路径，不覆盖原文件
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"✅ 已保存全部字段至：{output_path}")

def split_train_test_dev(file_path):
    # 1. 读取数据
    df = pd.read_csv(file_path)

    print(f"总样本数: {len(df)}")
    print("类别分布:\n", df['parent_category'].value_counts())

    # 2. 第一次拆分：训练集 80%，临时集 20%
    train_df, temp_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,  # 固定随机种子保证可复现
        stratify=df['parent_category']  # 按类别分层
    )

    # 3. 第二次拆分：临时集按 1:1 分为验证集和测试集（各占整体的 10%）
    dev_df, test_df = train_test_split(
        temp_df,
        test_size=0.5,  # 占临时集的 50%，即整体的 10%
        random_state=42,
        stratify=temp_df['parent_category']
    )

    # 4. 保存文件

    train_df.to_csv(config.train_path,index=False,encoding='utf-8')
    dev_df.to_csv(config.dev_path,index=False,encoding='utf-8')
    test_df.to_csv(config.test_path,index=False,encoding='utf-8')

    print(f"训练集大小: {len(train_df)} ({len(train_df) / len(df):.1%})")
    print(f"验证集大小: {len(dev_df)} ({len(dev_df) / len(df):.1%})")
    print(f"测试集大小: {len(test_df)} ({len(test_df) / len(df):.1%})")

    # 可选：验证每个集合的类别比例是否与原始一致
    print("\n训练集类别分布:\n", train_df['parent_category'].value_counts(normalize=True))

def load_category_mapping(txt_path):
    """读取类别索引文件，返回 {类别: 索引} 字典（索引从0开始）"""
    with open(txt_path, 'r', encoding='utf-8') as f:
        categories = [line.strip() for line in f if line.strip()]
    return {cat: idx for idx, cat in enumerate(categories)}


def convert_labels_inplace(file_path, mapping):
    """
    将 parent_category 映射为整数标签，删除原列，只保留 text 和 label，
    输出制表符分隔（覆盖原文件）。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return

    # 处理标题行：将 "parent_category,text" 改为 "text\tlabel"
    # 假设原列名可能是 text 或 title，但我们统一输出 text
    header = lines[0].strip()
    # 即使标题是 "parent_category,text"，我们直接忽略，强制写新标题
    new_lines = ["text\tlabel\n"]

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        # 只拆分第一个逗号
        parts = line.split(',', 1)
        if len(parts) != 2:
            print(f"⚠️ 跳过异常行（无逗号）：{line[:50]}...")
            continue
        category, text = parts[0], parts[1]
        label = mapping.get(category)
        if label is None:
            print(f"⚠️ 未知类别 '{category}'，跳过此行")
            continue
        new_lines.append(f"{text}\t{label}\n")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"✅ 转换完成：{file_path}")


def convert_all_labels(index_path):
    """
    主函数：读取类别映射，并转换训练、验证、测试集的标签。
    参数：
        config: Config 实例，包含 train_path, dev_path, test_path
        index_path: 类别索引文件路径（category_index.txt）
    """
    mapping = load_category_mapping(index_path)
    print(f"📋 共加载 {len(mapping)} 个类别映射")

    convert_labels_inplace(config.train_path, mapping)
    convert_labels_inplace(config.dev_path, mapping)
    convert_labels_inplace(config.test_path, mapping)

    print("🎯 所有文件标签转换完成！")


if __name__ == '__main__':
    # 保留原文件名加 _fixed）
    create_fix_csv(config.title_csv,config.title_fixed)
    split_train_test_dev(config.title_fixed)
    convert_all_labels(config.category_index)