# 导包
import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader,TensorDataset

# todo 提前准备数据
def data_preprocess():
    # 1.读取原始数据
    data = pd.read_csv('data/手机价格预测.csv')
    # print(data.shape)#(2000, 21)

    # 2.数据预处理
    data = data.dropna()
    # print(data.shape)#(2000, 21)

    # 3. 获取x特征和y标签
    x = data.iloc[:, 0:-1]
    y = data.iloc[:, -1]
    # print(x.shape, y.shape)#(2000, 20) (2000,)

    # 提前需改特征类型为float32
    x = x.astype(np.float32) # todo 后续张量要求特征都要是float32，可以提前转换也可以后续转换

    # 4. 划分训练集和测试集

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)#(1340, 20) (660, 20) (1340,) (660,)
    # todo 返回结果
    return x_train, x_test, y_train, y_test

def get_data_loader(batch_size):
    # 获取预处理数据
    x_train, x_test, y_train, y_test = data_preprocess()
    # todo 先封装dataset
    train_dataset = TensorDataset(torch.tensor(x_train.values), torch.tensor(y_train.values))
    test_dataset = TensorDataset(torch.tensor(x_test.values), torch.tensor(y_test.values))
    print(train_dataset[0])
    print(test_dataset[0])
    # todo 封装dataloader
    # 返回结果
    return DataLoader(train_dataset,batch_size,shuffle=True),DataLoader(test_dataset,batch_size,shuffle=False)

# todo 提前准备模型

# todo 模型训练api

# todo 模型评估api


if __name__ == '__main__':
    # 超参数
    batch_size = 4
    # todo 提前准备数据
    train_dataloader,test_dataloader = get_data_loader(batch_size)
    for batch in test_dataloader:
        print(batch)
        break
    # todo 提前准备模型
    # todo 开始模型训练
    # todo 开始模型评估