# 导包
import torch
# todo 先安装torchsummary，通过它帮助计算模型的参数
from torchsummary import summary
# todo 自定义神经网络模型-> 1个继承2个重写
# 1.继承torch.nn.Module
class MyModel(torch.nn.Module):
    # 2.重写__init__()和forward()
    def __init__(self, Input_size ,Output_size):
        super().__init__()
        # 神经网络层（3，3） -> （3，2） -> （2，2）
        self.fc1 = torch.nn.Linear(Input_size, 3)
        self.fc2 = torch.nn.Linear(3, 2)
        self.out = torch.nn.Linear(2, Output_size)
        #其实w和b都默认初始化，fc1的w泽维尔初始化，fc2的w凯明初始化
        torch.nn.init.xavier_uniform_(self.fc1.weight)
        torch.nn.init.kaiming_uniform_(self.fc2.weight)

    def forward(self, x):
        # 前隐藏层用sigmoid激活函数对加权求和的结果处理
        x = self.fc1(x)
        x = torch.sigmoid(x)
        # 深隐藏层用relu激活函数对加权求和结果处理
        x = self.fc2(x)
        x = torch.relu(x)
        # 输出层用softmax激活函数对加权求和结果处理
        x = self.out(x)
        x = torch.softmax(x, dim=1)
        return x

if __name__ == '__main__':
    # todo 模拟现有数据：5个样本3个特征，假设用softmax做的二分类
    # 输入特征数，输出分类结果
    batch_size = 5
    Input_size = 3
    Output_size = 2
    x = torch.randn(batch_size, Input_size)
    # todo 初始化模型
    model = MyModel(Input_size, Output_size) # 自动调用init
    # todo 调用模型
    Output = model(x) # 自动调用forward()
    print(Output)
    print("*"*60)
    # todo 演示如何快速计算参数量
    summary(model,(Input_size,))