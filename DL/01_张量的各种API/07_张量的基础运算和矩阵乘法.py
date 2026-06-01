# 导包
import torch

# 创建张量
t = torch.tensor([1, 3, 6],dtype=torch.float)
print(t)
print('--------')

# todo加减乘除
print(t + 2)
print(t.add(2))
print(t - 2)
print(t.sub(2))
print(t * 2)
print(t.mul(2))
print(t / 2)
print(t.div(2))

print('--------')
print(t)
print('--------')

#todo 加减乘除，直接修改原有张量
t.add_(2)
print(t)
t.sub_(2)
print(t)
t.mul_(2)
print(t)
t.div_(2)
print(t)

#todo 矩阵乘法
t1 = torch.tensor([[1,2,3],[4,5,6]])
t2 = torch.tensor([[1,2],[3,4],[5,6]])
print(t1,t1.shape)
print(t2,t2.shape)
#@
print(t1 @ t2)
#matmul()
print(t1.matmul(t2))
print('-'*30)
#todo 注意：矩阵乘法不满足交换律
print(t2 @ t1)
print(t2.matmul(t1))