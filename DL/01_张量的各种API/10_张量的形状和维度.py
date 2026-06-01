# 导包
import torch
# TODO reshape（）：修改形状，维度可能跟着改变
# 创建张量
# t = torch.tensor([i for i in range(1,11)])
# print(t,t.shape)
t2 = torch.randint(low=1,high=11,size=(10,))
print(t2,t2.shape)

#reshape()应用
t3 = t2.reshape(2,5)
print(t3,t3.shape,t3.ndim)
t3 = t2.reshape(5,2)
print(t3,t3.shape,t3.ndim)
t3 = t2.reshape(1,10)
print(t3,t3.shape,t3.ndim)
t3 = t2.reshape(10,1)
print(t3,t3.shape,t3.ndim)

t3 = t2.reshape(1,1,10)
print(t3,t3.shape,t3.ndim)
t3 = t2.reshape(10,1,1)
print(t3,t3.shape,t3.ndim)

t4 = torch.tensor([i for i in range(20)])
print(t4.reshape(4,-1))
print(t4.reshape(2,-1))
print(t4.reshape(5,-1))
print(t4.reshape(-1,5))
print(t4.reshape(-1,4))
print(t4.reshape(-1,10))
print(t4.reshape(-1,2))
print(t4.reshape(-1,1))
print(t4.reshape(-1))

# todo squeeze():降维，删除维度值为1的维度
print(t3,t3.shape,t3.ndim)
t5 = t3.squeeze()
print(t5,t5.shape,t5.ndim)
# todo unsqueeze():升维，增加维度值为1的维度
t6 = t5.unsqueeze(-1).unsqueeze(0)
print(t6,t6.shape,t6.ndim)

# todo permute():一次交换多个维度
t6 = torch.randint(1,6,(3,2,4))
t7 = t6.permute(2,0,1)
print(t7.shape,t7.ndim)
# todo：transpose():一次交换两个维度
t8 = t6.transpose(1,2).transpose(0,1)
print(t8.shape,t8.ndim)
# todo view()只能改连续的张量
t9 = torch.tensor([[1,5,3],[6,2,4]])
print(t9.shape,t9.is_contiguous())
print(t9.view(1,6))
#todo reshape()可以改变形状
print(t9.reshape(6,1))



