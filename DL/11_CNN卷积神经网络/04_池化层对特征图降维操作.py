# 导包
import torch
# 准备数据
t1 = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]]])
print(t1,t1.shape)

# 最大池化
pool1 = torch.nn.MaxPool2d(kernel_size=2,stride=1,padding=0)
out1 = pool1(t1)
print(out1)
# 平均池化
pool2 =torch.nn.AvgPool2d(kernel_size=2,stride=1,padding=0)
out2 = pool2(t1)
print(out2)

print("--"*30)
# 准备数据
t1 = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]],
                   [[11,22,33],[44,55,66],[77,88,99]],
                   [[19,28,37],[46,55,64],[73,82,91]]])
print(t1,t1.shape)

# 最大池化
pool1 = torch.nn.MaxPool2d(kernel_size=2,stride=1,padding=0)
out1 = pool1(t1)
print(out1)
# 平均池化
pool2 =torch.nn.AvgPool2d(kernel_size=2,stride=1,padding=0)
out2 = pool2(t1)
print(out2)

