import pandas as pd
import jieba
from tqdm import tqdm
from config.config import Config

config = Config()

def process_data(base_path, process_path):
    # 1. 读取数据（指定 sep='\t'，因为您之前已转换为制表符分隔）
    df_data = pd.read_csv(base_path, sep='\t')

    # 2. 使用 tqdm 显示进度条：对每一行分词
    #    方法1：使用 tqdm.pandas() 和 progress_apply
    tqdm.pandas(desc="分词处理")
    df_data['words'] = df_data['text'].progress_apply(lambda x: " ".join(jieba.lcut(x)))

    #    方法2（备选）：如果不想用 progress_apply，也可以手动循环 + tqdm
    #    words = []
    #    for text in tqdm(df_data['text'], desc="分词处理"):
    #        words.append(" ".join(jieba.lcut(text)))
    #    df_data['words'] = words

    # 3. 保存数据
    df_data.to_csv(process_path, sep='\t', index=False, header=True)
    print(f"✅ 已保存：{process_path}")

if __name__ == '__main__':
    process_data(config.train_path, config.process_train_path)
    process_data(config.dev_path, config.process_dev_path)
    process_data(config.test_path, config.process_test_path)