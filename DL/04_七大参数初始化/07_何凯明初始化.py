# 导包
import torch

# TODO 模拟构建全连接网络层
fc = torch.nn.Linear(5, 3)
# TODO 何凯明均匀分布初始化
torch.nn.init.kaiming_uniform_(fc.weight)
# 查看修改后的权重
print(f"初始化权重:{fc.weight}")
print('=============================================')
# TODO 何凯明正态分布初始化
torch.nn.init.kaiming_normal_(fc.weight)
# 查看修改后的权重
print(f"初始化权重:{fc.weight}")

