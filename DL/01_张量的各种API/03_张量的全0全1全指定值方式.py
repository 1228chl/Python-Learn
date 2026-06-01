# 导包
import torch

# 创建全0张量
t1 = torch.zeros(size=(3, 4))
print(t1, type(t1), t1.dtype, t1.ndim, t1.shape)
# 创建全1张量
t1 = torch.ones(size=(3, 4))
print(t1, type(t1), t1.dtype, t1.ndim, t1.shape)
# 创建全指定值张量
t1 = torch.full(size=(3, 4), fill_value=8.0)
print(t1, type(t1), t1.dtype, t1.ndim, t1.shape)

print('=' * 80)

# 先创建一个张量,参考它的形状,再创建全0全1全指定值的张量
t2 = torch.tensor([[1, 2, 3], [3, 4, 5]])
# 全0
t3 = torch.zeros_like(t2)
print(t3, type(t3), t3.dtype, t3.ndim, t3.shape)
# 全1
t3 = torch.ones_like(t2)
print(t3, type(t3), t3.dtype, t3.ndim, t3.shape)
# 全指定值
t3 = torch.full_like(t2, fill_value=8.0)
print(t3, type(t3), t3.dtype, t3.ndim, t3.shape)

