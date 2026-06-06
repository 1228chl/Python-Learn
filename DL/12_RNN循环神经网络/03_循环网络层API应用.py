#导包
import torch
# 1.模拟准备Xt词向量数据
# 模型2个样本，每个样本5个字，每个字6个维度
x = torch.randn(size=(5,2,6))
print(f'2个样本，每个样本5个词：\n{x}')
# 2. 模拟准备隐藏状态
# 处理2个样本，1个隐藏层，每个字输出12个维度
h0 = torch.zeros(size=(1,2,12))
# 3.创建RNN层并预测
rnn = torch.nn.RNN(input_size=6,hidden_size=12,num_layers=1,batch_first=False)
y,hn = rnn(x,h0)
print(hn.shape)
print(y.shape)

print("="*60)
# 1.模拟准备Xt词向量数据
# 模型2个样本，每个样本5个字，每个字6个维度
x = torch.randn(size=(2,5,6))
print(f'2个样本，每个样本5个词：\n{x}')
# 2. 模拟准备隐藏状态
# 处理2个样本，1个隐藏层，每个字输出12个维度
h0 = torch.zeros(size=(1,2,12))
# 3.创建RNN层并预测
rnn = torch.nn.RNN(input_size=6,hidden_size=12,num_layers=1,batch_first=True)
y,hn = rnn(x,h0)
print(hn.shape)
print(y.shape)
