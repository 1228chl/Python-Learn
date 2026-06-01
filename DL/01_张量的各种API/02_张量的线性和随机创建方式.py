# 导包
import torch
#todo 1.1线性方式 arange(开始,结束(不含),步长)

t1 = torch.arange(start=1, end=10, step=1)
print(t1,t1.dtype)
#todo 1.2线性方式 linspace(开始,结束(含),个数)
t2 = torch.linspace(start=1,end=10,steps=10)
print(t2,t2.dtype)

print("="*60)

#todo 提前设置种子
torch.manual_seed(666)
print(f"种子：{torch.initial_seed()}")
#todo 2.1随机方式rand(size=形状)：默认生成0-1的浮点数
t3 = torch.rand(size=(2,2,3))
print(t3,t3.shape)
#todo 2.2随机方式randn(size=形状)：默认生成正态分布的浮点数
t3 = torch.randn(size=(2,2,3))
print(t3,t3.shape)
#todo 2.3随机方式randint(start,end,size=形状)：默认生成0-end的整数
t3=torch.randint(low=1,high=10,size=(2,2,3))#不含high
print(t3,t3.shape)