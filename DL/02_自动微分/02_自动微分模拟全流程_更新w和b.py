# 导包
import torch

# 1.模拟准备X样本数据(2个样本,每个样本5个特征)
x = torch.rand(size=(2, 5))
# 2.模拟准备Y标签数据
y = torch.zeros(size=(2, 3))
# 3.初始化w和b
w = torch.randn(size=(5, 3),requires_grad=True)
b = torch.zeros(size=(3,),requires_grad=True)
print(x)
print(y)
print(w)
print(b)
print('===================================')
# TODO 模拟前向传播  z = xw+b
z = x @ w + b
# TODO 模拟计算损失
loss_fn = torch.nn.MSELoss()
loss = loss_fn(z,y)
# TODO 模拟反向传播
loss.sum().backward()
# 获取梯度
# print(w.grad)
# print(b.grad)
w1 = w - 0.01 * w.grad
print(w1)
b1 = b - 0.01 * b.grad
print(b1)