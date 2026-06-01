import torch
# todo 1.单独数字转换为张量
a1 = 10
print(type(a1),a1)
#transform
t1 = torch.tensor(a1)
print(type(t1),t1)

print("="*30)

#todo 2.张量转换为数字
t2 = torch.tensor(100)
print(type(t2),t2)
print(t2.item())

t3 = torch.tensor([100])
print(type(t3),t3)
print(t3.item())

t4 = torch.tensor([[100]])
print(type(t4),t4)
print(t4.item())



