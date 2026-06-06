# 导包
import pandas as pd
import numpy as np
import torch
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader,TensorDataset

# 提前准备数据
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
    x = x.astype(np.float32) # 后续张量要求特征都要是float32，可以提前转换也可以后续转换
    y = y.astype(np.int64)
    # 4. 划分训练集和测试集

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)#(1340, 20) (660, 20) (1340,) (660,)
    # 优化1：标准化
    ss = StandardScaler()
    x_train = ss.fit_transform(x_train)# 底层自动转换为numpy类型
    x_test = ss.transform(x_test)
    # 返回结果
    return x_train, x_test, y_train, y_test

def get_data_loader(batch_size):
    # 获取预处理数据
    x_train, x_test, y_train, y_test = data_preprocess()
    # 先封装dataset
    train_dataset = TensorDataset(torch.tensor(x_train), torch.tensor(y_train.values))
    test_dataset = TensorDataset(torch.tensor(x_test), torch.tensor(y_test.values))
    # print(train_dataset[0])
    # print(test_dataset[0])
    # 封装dataloader
    train_dataloader = DataLoader(train_dataset,batch_size,shuffle=True)
    test_dataloader = DataLoader(test_dataset,batch_size,shuffle=False)
    # 返回结果
    return train_dataloader,test_dataloader

# 提前准备模型
class PhoneModel(torch.nn.Module):
    def __init__(self,input_size,output_size):
        super(PhoneModel, self).__init__()
        self.l1 = torch.nn.Linear(input_size, 128)
        self.l2 = torch.nn.Linear(128, 256)
        # 优化2：增加层数
        self.l3 = torch.nn.Linear(256, 512)
        self.l4 = torch.nn.Linear(512, 256)
        self.l5 = torch.nn.Linear(256, 128)
        self.out = torch.nn.Linear(128, output_size)

    def forward(self, batch_x):
        batch_x = torch.relu(self.l1(batch_x))
        batch_x = torch.relu(self.l2(batch_x))
        batch_x = torch.relu(self.l3(batch_x))
        batch_x = torch.relu(self.l4(batch_x))
        batch_x = torch.relu(self.l5(batch_x))
        logits = self.out(batch_x)
        return logits
# 模型训练api
def model_train(train_dataloader,model:PhoneModel,epoch_num,model_path):
    # 准备数据（已经提前准备好了）
    # 准备模型（已经提前准备好了）
    model.train()
    # 准备损失函数
    loss_fn = torch.nn.CrossEntropyLoss(reduction='mean')
    # 准备优化器
    # optimizer = torch.optim.SGD(model.parameters(),lr=1e-3,momentum=0.9)
    # 优化3： 修改优化器和学习率
    optimizer = torch.optim.Adam(model.parameters(),lr=1e-3,betas=(0.9,0.999))
    # 外层遍历控制轮次
    for epoch in range(epoch_num):
        # 提前定义参数，为了打印日志
        total_loss = 0.0
        batch_cnt = 0
        start_time = time.time()
        # 内层遍历控制批次
        for batch_x,batch_y in train_dataloader:
            # 前向传播
            logits = model(batch_x)
            # 计算损失
            loss = loss_fn(logits,batch_y)
            # 累加损失，用于打印日志
            total_loss += loss.item()
            batch_cnt += 1
            # 梯度清零
            optimizer.zero_grad()
            # 反向传播
            loss.backward()
            # 参数更新
            optimizer.step()
        # 打印日志
        print(f"第{epoch+1}轮，损失为{total_loss/batch_cnt:.5f},时间:{time.time()-start_time:.2f}秒")
    # 保存模型
    torch.save(model.state_dict(),model_path)
# 模型评估api
def model_eval(test_dataloader,input_size,output_size,model_path):
    # 准备数据（已经提前准备好了）
    # 准备模型
    model = PhoneModel(input_size,output_size)
    model.load_state_dict(torch.load(model_path))
    model.eval()

    # 优化5： 评估阶段禁用梯度计算
    with torch.no_grad():
        # 训练遍历批次
        # 提前创建一个变量记录预测正确的数量
        pred_true = 0
        for batch_x,batch_y in test_dataloader:
            # 前向传播
            batch_logits = model(batch_x)
            # 累加预测结果
            batch_preds = torch.argmax(batch_logits, dim=-1)
            # print(f"预测标签{batch_preds}")
            # print(f"真实标签{batch_y}")
            pred_true += (batch_preds == batch_y).sum().item()
            # print(f"截止到当前批次预测正确的数量{pred_true}个")

        # 计算准确率
        acc = pred_true / len(test_dataloader.dataset)
        print(f"模型准确率{acc:.4f}")



if __name__ == '__main__':
    # 各种参数和路径
    input_size = 20
    output_size = 4
    # 优化4：优化轮次和批次
    batch_size = 16
    epoch_num = 50
    model_path = './model/phone_model.pth'
    # 提前准备数据
    train_dataloader,test_dataloader = get_data_loader(batch_size)
    # for batch in test_dataloader:
    #     print(batch)
    #     break
    # 提前准备模型

    model = PhoneModel(input_size,output_size) # 自动调用__init__()
    # 开始模型训练
    model_train(train_dataloader,model,epoch_num,model_path)
    # 开始模型评估
    model_eval(test_dataloader,input_size,output_size,model_path)