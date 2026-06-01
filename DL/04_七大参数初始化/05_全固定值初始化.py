# 导包
import torch

# todo 模拟构建全连接网络层
fc =torch.nn.Linear(5,3)
# 查看是否有初始权重和偏置
print(f"默认权重：{fc.weight}")
print(f"默认偏置：{fc.bias}")
print("-"*60)
# todo 自己初始化参数
torch.nn.init.constant_(fc.weight,6)
torch.nn.init.constant_(fc.bias,6)
# 查看修改后的权重偏置
print(f"初始化权重：{fc.weight}")
print(f"初始化偏置：{fc.bias}")
