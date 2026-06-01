# 导包
import torch

# todo 1.tensor（data=数据，dytype=类型）方式
t1 = torch.tensor(data=10)
print(t1,t1.ndim,t1.shape,t1.dtype)
t1 = torch.tensor(data=[10],dtype=torch.float32)
print(t1,t1.ndim,t1.shape,t1.dtype)
t1 = torch.tensor(data=[10,20,30],dtype=torch.float32)
print(t1,t1.ndim,t1.shape,t1.dtype)
t1 = torch.tensor(data=[[10,20,30],[11,22,33]],dtype=torch.float32)
print(t1,t1.ndim,t1.shape,t1.dtype)

print('#'*60)

#todo 2.Tensor（数据，size=形状）方式
t2 = torch.Tensor([10,20,30])
print(t2,t2.ndim,t2.shape,t2.dtype)
t2 = torch.Tensor(size=[2,3])
print(t2,t2.ndim,t2.shape,t2.dtype)

#todo 2.类型Tensor（）方式
t2 = torch.FloatTensor([10,20,30])
print(t2,t2.ndim,t2.shape,t2.dtype)
t2 = torch.IntTensor([10,20,30])
print(t2,t2.ndim,t2.shape,t2.dtype)


