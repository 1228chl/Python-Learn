import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import time

# set seed
torch.manual_seed(0)
np.random.seed(0)


def create_data(csv_path='data/手机价格预测.csv', test_size=0.2, random_state=88):
    """
        加载数据，划分训练/验证集，并进行标准化
        返回：训练集 Dataset 对象、验证集 Dataset 对象、输入维度、类别数
        """
    # 1. 读取数据
    data = pd.read_csv(csv_path)
    x = data.iloc[:, :-1].values.astype(np.float32)
    y = data.iloc[:, -1].values.astype(np.int64)

    # 2. 划分训练集和验证集（80% 训练，20% 验证）
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y  # 分层采样保证类别分布一致
    )

    # 3. 标准化（重要！可显著提升收敛速度和稳定性）
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # 4. 转换为 PyTorch 张量
    train_dataset = TensorDataset(torch.from_numpy(x_train), torch.from_numpy(y_train))
    test_dataset = TensorDataset(torch.from_numpy(x_test), torch.from_numpy(y_test))

    input_dim = x.shape[1]  # 特征数量（本例为 20）
    num_classes = len(np.unique(y))  # 类别数量（本例为 4）

    return train_dataset, test_dataset, input_dim, num_classes

# 基础版本
class PhonePriceModel(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(PhonePriceModel, self).__init__()
        self.linear1 = nn.Linear(input_dim,128)
        self.linear2 = nn.Linear(128,256)
        self.linear3 = nn.Linear(256,num_classes)

    def forward(self, x):
        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        output = self.linear3(x) # 后续 CrossEntropyLoss 中包含 softmax
        return output

# 训练函数（基础版）
def train(train_dataset,input_dim,class_num):
    torch.manual_seed(0)
    dataloader = DataLoader(train_dataset,shuffle=True,batch_size=8)
    model = PhonePriceModel(input_dim,class_num)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(),lr=1e-3)
    num_epoch = 50

    for epoch_idx in range(num_epoch):
        start = time.time()
        total_loss = 0.0
        total_num = 0
        for x,y in dataloader:
            output = model(x)
            loss = criterion(output,y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_num += len(y)
            total_loss += loss.item() * len(y)
        print('epoch:%4s loss: %2f,time:%2fs'%(epoch_idx,total_loss/total_num,time.time()-start))

        torch.save(model.state_dict(),'model/phone.pth')


# 评估函数
def test(test_dataset,input_dim,class_num,model_path='model/phone.pth'):
    model = PhonePriceModel(input_dim,class_num)
    model.load_state_dict(torch.load(model_path))
    dataloader = DataLoader(test_dataset,shuffle=False,batch_size=8)
    correct = 0
    for x,y in dataloader:
        model.eval()
        output = model(x)
        y_pred = torch.argmax(output,dim=1)
        correct += (y_pred == y).sum().item()
    print('Acc: %.5f' % (correct/len(test_dataset)))

if __name__ == '__main__':
    train_dataset,test_dataset,input_dim,class_num = create_data()
    # 基础版本训练
    train(train_dataset,input_dim,class_num)
    test(test_dataset,input_dim,class_num)













