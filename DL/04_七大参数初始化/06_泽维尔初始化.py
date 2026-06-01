# 导包
import torch

# TODO 模拟构建全连接网络层
fc = torch.nn.Linear(5, 3)
# TODO 泽维尔均匀分布初始化
torch.nn.init.xavier_uniform_(fc.weight)
# 查看修改后的权重
print(f"初始化权重:{fc.weight}")
print('=============================================')
# TODO 泽维尔正态分布初始化
torch.nn.init.xavier_normal_(fc.weight)
# 查看修改后的权重
print(f"初始化权重:{fc.weight}")

