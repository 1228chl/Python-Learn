import pandas as pd
import jieba
from _01_config import Config

# 提前创建Config对象
config = Config()


# 定义处理数据的函数
def process_data(base_path, process_path):
    # 1.读取数据
    df_data = pd.read_csv(base_path, sep='\t', names=['text', 'label'])
    # 2.apply()对每一行进行分词并存储为一列
    df_data['words'] = df_data['text'].apply(lambda x: " ".join(jieba.lcut(x)))
    # print(df_data) # 测试
    # 3.保存数据
    df_data.to_csv(process_path, sep='\t', index=False, header=True)


if __name__ == '__main__':
    # 处理训练数据
    process_data(config.train_path, config.process_train_path)
    # 处理验证数据
    process_data(config.dev_path, config.process_dev_path)
    # 处理测试数据
    process_data(config.test_path, config.process_test_path)
