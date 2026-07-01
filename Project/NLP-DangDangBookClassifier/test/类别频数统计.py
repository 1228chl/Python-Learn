import pandas as pd
from config.config import Config

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

    # 查看合并后的分布（只显示前10个，避免刷屏）
    print("合并后各类别数量（前10个）：")
    print(df['parent_category'].value_counts().head(10))

    # 保存到新路径，不覆盖原文件
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"✅ 已保存全部字段至：{output_path}")

if __name__ == '__main__':
    # 定义输出路径（放在 data/processed/ 目录下，保留原文件名加 _fixed）
    import os
    os.makedirs(config.root_path + 'data/processed/', exist_ok=True)

    create_fix_csv(
        config.title_csv,
        config.root_path + 'data/processed/title_fixed.csv'
    )
    create_fix_csv(
        config.intro_csv,
        config.root_path + 'data/processed/intro_fixed.csv'
    )
    create_fix_csv(
        config.title_intro_csv,
        config.root_path + 'data/processed/title_intro_fixed.csv'
    )