from collections import Counter
import pandas as pd
from config import Config



def data_eda(path):
    # 第一步：读取数据并查看基本信息
    df_data = pd.read_csv(path,sep='\t',header=None,names=['test','label'])
    # 打印前10行
    print(df_data.head(10))
    # 总数据量
    print(len(df_data))
    print("*"*100 +'\n\n\n')

    # 第二步：了解类别分布情况是否均衡
    counters = Counter(df_data['label'])
    print(counters)
    # 也可以计算每个类别数据量占比
    all_cnt = len(df_data)
    for k,v in counters.items():
        print(f'类别 {k} 的数据占比为：{(v/all_cnt * 100)}%')
    print("*" * 100 + '\n\n\n')

    # 第三步：了解文本长度分布情况
    # 获取每个文本的长度并作为一列存储到df_data中
    df_data['text_len'] = df_data['test'].apply(lambda x: len(x))
    # print(df_data)
    # 统计平均长度，最大长度，最小长度，标准差
    print(f'平均长度为：{df_data["text_len"].mean()}')
    print(f'最大长度为：{df_data["text_len"].max()}')
    print(f'最小长度为：{df_data["text_len"].min()}')
    print(f'标准差为：{df_data["text_len"].std()}')
if __name__ == '__main__':
    # 创建配置对象，获取配置参数
    c = Config()
    # 查看训练数据情况
    data_eda(c.train_path)
    print("="*90)
    # 查看验证数据情况
    data_eda(c.dev_path)
    print("="*90)
    # 查看测试数据情况
    data_eda(c.test_path)