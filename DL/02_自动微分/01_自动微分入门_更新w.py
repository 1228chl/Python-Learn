# 导包
import torch

# 模拟初始W权重参数
# TODO 开启自动微分
w = torch.tensor(data=[10.0, 20.0], requires_grad=True)
print(f"初始参数:{w.data},初始梯度:{w.grad}")
# 模拟损失函数计算损失
loss = 2 * w ** 2
print(loss)  # tensor([200., 800.])
# TODO 反向传播自动计算梯度,放到grad属性中
loss.sum().backward()
# TODO 获取计算完的梯度
print(f"最新梯度:{w.grad}")
# 更新w权重 : 新参数 = 旧参数 - 学习率*梯度
w1 = w - 0.01 * w.grad
print(f"最新参数:{w1}")
