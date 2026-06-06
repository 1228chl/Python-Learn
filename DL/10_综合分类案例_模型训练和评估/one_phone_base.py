import pandas as pd
import numpy as np
import torch
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader,TensorDataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device:{device}")

# 数据准备
def data_prepare():
    # read data
    data = pd.read_csv('data/手机价格预测.csv')

    data = data.dropna()

    x = data.iloc[:,0:-1]
    y = data.iloc[:,-1]

    x = x.astype(np.float32)
    y = y.astype(np.int64)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    return x_train,x_test,y_train,y_test

def get_data_loader(batches):
    x_train,x_test,y_train,y_test = data_prepare()

    train_dataset = TensorDataset(torch.tensor(x_train),torch.tensor(y_train.values))
    test_dataset = TensorDataset(torch.tensor(x_test),torch.tensor(y_test.values))

    train_dataloader = DataLoader(train_dataset,batches,True)
    test_dataloader = DataLoader(test_dataset,batches,False)

    return train_dataloader,test_dataloader

class PhoneModel(torch.nn.Module):
    def __init__(self,input_size,output_size):
        super().__init__()
        self.l1 = torch.nn.Linear(input_size,128)
        self.l2 = torch.nn.Linear(128,256)
        self.out = torch.nn.Linear(256,output_size)

    def forward(self,batch_x):
        batch_x = torch.relu(self.l1(batch_x))
        batch_x = torch.relu(self.l2(batch_x))
        logits = self.out(batch_x)
        return logits

def model_train(train_dataloader,model:PhoneModel,epoch_num,model_path):
    # 关键1：把模型移到 GPU
    model.to(device)
    model.train()
    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(),0.01,(0.9,0.999))
    for epoch in range(epoch_num):
        total_loss = 0.0
        batch_cnt = 0
        start_time = time.time()
        for batch_x,batch_y in train_dataloader:
            # 关键2：把数据移到 GPU
            batch_x,batch_y=batch_x.to(device),batch_y.to(device)
            logits = model(batch_x)
            loss = loss_fn(logits,batch_y)
            total_loss += loss.item()
            batch_cnt += 1
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"第{epoch+1}轮，损失为{total_loss/batch_cnt:.5f},时间:{time.time()-start_time:.2f}秒")

    torch.save(model.state_dict(),model_path)

def model_eval(test_dataloader,input_size,output_size,model_path):
    model = PhoneModel(input_size,output_size)
    # 关键3：加载模型时先映射到 CPU 或 GPU，然后整体移到设备
    state_dict = torch.load(model_path,map_location=device)
    model.load_state_dict(state_dict)
    model.to(device)# 把模型移到 GPU
    model.eval()

    with torch.no_grad():
        pred_true = 0
        for batch_x,batch_y in test_dataloader:
            # 关键4：评估时数据也要移到 GPU
            batch_x,batch_y = batch_x.to(device),batch_y.to(device)
            batch_logits = model(batch_x)
            batch_preds = torch.argmax(batch_logits,dim=-1)
            pred_true += (batch_preds == batch_y).sum().item()

        acc = pred_true / len(test_dataloader.dataset)
        print(f"模型准确率{acc:.4f}")

if __name__ == '__main__':
    input_size = 20
    output_size = 4
    batches = 16
    epoch_num = 60
    model_path = './model/phone_model.pth'
    train_dataloader,test_dataloader = get_data_loader(batches)
    model = PhoneModel(input_size,output_size)
    model_train(train_dataloader,model,epoch_num,model_path)
    model_eval(test_dataloader,input_size, output_size, model_path)


