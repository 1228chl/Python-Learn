# 导包
import torch

# TODO 模拟准备图像数据
# 图像格式(N, C, H, W) N=1 (batch size), C=3 (channels), H=5 (height), W=5 (width)
x = torch.randint(1, 10, size=(1, 3, 5, 5), dtype=torch.float)
print(x)
# TODO 模拟创建BN层并处理数据
# BatchNorm2d的输入张量形状通常是 (N, C, H, W)。
bn = torch.nn.BatchNorm2d(num_features=3)
out = bn(x)
print(out)