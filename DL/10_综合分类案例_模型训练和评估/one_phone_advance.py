import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# set seed
torch.manual_seed(1)
np.random.seed(2)


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

# 进阶版本模型（带 BatchNorm、Dropout、Kaiming 初始化）
class PhonePriceModelAdvanced(nn.Module):
    def __init__(self, input_dim,output_dim,hidden_dims,dropout_rate=0.3):
        super(PhonePriceModelAdvanced, self).__init__()
        self.fc1 = nn.Linear(input_dim,hidden_dims[0])
        self.bn1 = nn.BatchNorm1d(hidden_dims[0])
        self.dropout1 = nn.Dropout(dropout_rate)

        self.fc2 = nn.Linear(hidden_dims[0],hidden_dims[1])
        self.bn2 = nn.BatchNorm1d(hidden_dims[1])
        self.dropout2 = nn.Dropout(dropout_rate)

        self.fc3 = nn.Linear(hidden_dims[1], hidden_dims[2])
        self.bn3 = nn.BatchNorm1d(hidden_dims[2])
        self.dropout3 = nn.Dropout(dropout_rate)

        self.fc4 = nn.Linear(hidden_dims[2], hidden_dims[3])
        self.bn4 = nn.BatchNorm1d(hidden_dims[3])
        self.dropout4 = nn.Dropout(dropout_rate)

        self.out = nn.Linear(hidden_dims[3],output_dim)
        # self.out = nn.Linear(hidden_dims[1],output_dim)

        self._initialize_weights()

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.kaiming_uniform_(m.weight,mode='fan_in',nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias,0)

    def forward(self, x):
        x = self.fc1(x)
        x = self.bn1(x)
        x = torch.relu(x)
        x = self.dropout1(x)

        x = self.fc2(x)
        x = self.bn2(x)
        x = torch.relu(x)
        x = self.dropout2(x)

        x = self.fc3(x)
        x = self.bn3(x)
        x = torch.relu(x)
        x = self.dropout3(x)

        x = self.fc4(x)
        x = self.bn4(x)
        x = torch.relu(x)
        x = self.dropout4(x)

        x = self.out(x)

        return x


# 训练函数（进阶版，带早停和学习率调度）
def train_model(
        model,
        train_dataset,
        test_dataset,
        batch_size=64,
        lr=0.001,
        weight_decay=1e-4,
        num_epochs=100,
        patience=10):
    train_loader = DataLoader(train_dataset,batch_size=batch_size,shuffle=True)
    test_loader = DataLoader(test_dataset,batch_size=batch_size,shuffle=False)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(),lr=lr,weight_decay=weight_decay)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5)
    best_test_acc = 0.0
    best_epoch = 0
    epochs_no_improve = 0

    train_losses = []
    test_accs = []

    for epoch in range(1,num_epochs+1):
        # 训练阶段
        model.train()
        total_loss = 0.0
        for x_batch,y_batch in train_loader:
            x_batch, y_batch = x_batch.to(device), y_batch.to(device)  # 添加这行
            optimizer.zero_grad()
            outputs = model(x_batch)
            loss = criterion(outputs,y_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * x_batch.size(0)
        avg_train_loss = total_loss / len(train_dataset)
        train_losses.append(avg_train_loss)

        # 验证阶段
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for x_batch,y_batch in test_loader:
                x_batch, y_batch = x_batch.to(device), y_batch.to(device)  # 添加这行
                outputs = model(x_batch)
                _,preds = torch.max(outputs,dim=1)
                correct += (preds == y_batch).sum().item()
                total += y_batch.size(0)
        test_acc = correct/total
        test_accs.append(test_acc)

        scheduler.step(avg_train_loss)

        # if epoch %10 == 0 or epoch == 1:
        #     print(f'Epoch [{epoch}/{num_epochs}], Loss: {avg_train_loss:.4f}, Test Acc: {test_acc:.4f}')
        print(f'Epoch [{epoch}/{num_epochs}], Loss: {avg_train_loss:.4f}, Test Acc: {test_acc:.4f}')

        # 早停与保存最佳模型
        if test_acc > best_test_acc:
            best_test_acc = test_acc
            best_epoch = epoch
            torch.save(model.state_dict(), 'model/best_phone_model.pth')
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1
            if epochs_no_improve >= patience:
                print(f"Early stopping at epoch {epoch}, best test acc: {best_test_acc:.4f} at epoch {best_epoch}")
                break

    model.load_state_dict(torch.load('model/best_phone_model.pth'))
    return model,best_test_acc,train_losses,test_accs

if __name__ == '__main__':
    train_dataset,test_dataset,input_dim,class_num = create_data()
    model = PhonePriceModelAdvanced(input_dim,
                                    class_num,
                                    hidden_dims=[128,256,256,256],
                                    dropout_rate=0.3)
    model = model.to(device) # 将模型导入GPU


    train_model,best_acc,losses,accs = train_model(
        model,
        train_dataset,
        test_dataset,
        batch_size=64,
        lr=1e-3,
        weight_decay=1e-4,
        num_epochs=100,
        patience=50
    )
    print(f"最佳验证集准确率: {best_acc:.5f}")
    # 绘制训练曲线和混淆矩阵等















