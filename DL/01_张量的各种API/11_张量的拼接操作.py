#模拟准备操作
import torch

torch.manual_seed(1)
t1 = torch.randint(1, 10, size=(3, 4))
t2 = torch.randint(1, 10, size=(3, 4))
print(t1,t1.shape)
print(t2,t2.shape)
# todo:cat()：直接在指定维度上拼接，不会产生新的维度
# 注意：除了拼接维度外，其他维度必须相同
c1 = torch.cat([t1, t2],0)
print(c1,c1.shape)
c2 = torch.cat([t1, t2],1)
print(c2,c2.shape)
print('='*50)
# todo:stack()：在指定维度上先升维，再拼接
# 注意：要求拼接的每个张量纬度值都要一致
s1 = torch.stack([t1, t2],0)
print(s1,s1.shape)
s2 = torch.stack([t1, t2],1)
print(s2,s2.shape)
s3 = torch.stack([t1, t2],2)
print(s3,s3.shape)