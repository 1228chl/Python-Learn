# 导包
import torch

# TODO 1.模拟准备Xt词向量数据
# 模型2个样本,每个样本5个字,每个字6维度
"""
我很爱你哦
我非常想你
"""
x = torch.randn(size=(5, 2, 6))
# print(f"2个样本,每个样本5个词:\n{x}")
# TODO 2.模拟准备隐藏状态
# 处理2个样本,1个隐藏层,每个字输出12个维度
h0 = torch.zeros(size=(1, 2, 12))
# TODO 3.创建RNN层并预测
rnn = torch.nn.RNN(input_size=6, hidden_size=12, num_layers=1, batch_first=False)
y, hn = rnn(x, h0)
print(hn)  # 和h0形状一模一样
print(y)  # 样本数和句子词数和x一样,输出词向量维度和隐藏层维度一致

print('=========================================================================')
# TODO 1.模拟准备Xt词向量数据
# 模型2个样本,每个样本5个字,每个字6维度
"""
我很爱你哦
我非常想你
"""
x = torch.randn(size=(2, 5, 6))
# print(f"2个样本,每个样本5个词:\n{x}")
# TODO 2.模拟准备隐藏状态
# 处理2个样本,1个隐藏层,每个字输出12个维度
h0 = torch.zeros(size=(1, 2, 12))
# TODO 3.创建RNN层并预测
rnn = torch.nn.RNN(input_size=6, hidden_size=12, num_layers=1, batch_first=True)
y, hn = rnn(x, h0)
print(hn)  # 和h0形状一模一样
print(y)  # 样本数和句子词数和x一样,输出词向量维度和隐藏层维度一致
