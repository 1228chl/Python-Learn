# 导包
import torch
# 创建张量并开启自动微分
t1 = torch.tensor([10,20],requires_grad=True,dtype=torch.float32)
print(t1.requires_grad)
# 开启了自动微分的张量不能直接转为Numpy
# n1 = t1.numpy()# 报错
# print(n1)
# 已经开启了自动微分的张量，如何转换numpy？
# 先用detach()拷贝并关闭自动微分，然后再转numpy
t2 = t1.detach()
print(t2,t2.requires_grad)
# detach()后的张量就可以转numpy了
n1 = t2.numpy()
print(n1,type(n1))

# 1.detach()和原始张量共享内存，但是额外关闭了自动微分
# 注意：detach()后的张量和原始张量共享内存
t2[0] = 100
print(t2)
print(t1)

# 2.clone()是把原始张量数据和属性都拷贝,并重新开辟了新空间
t3 = t1.clone()
print(t3)
t3[1] = 200
print(t3)
print(t1)

print('='*80)
# 上述是通过对比修改前后变化,判断是否共享内存
# 通过元素内存地址判断是否共享内存
print(id(t1),id(t2),id(t3))
print(t1.data_ptr(),t2.data_ptr(),t3.data_ptr())