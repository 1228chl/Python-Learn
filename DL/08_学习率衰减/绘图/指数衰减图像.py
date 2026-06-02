import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 创建模型和优化器
model = nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# 创建 ExponentialLR 调度器
gamma = 0.95
scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=gamma)

epochs = 100
lr_list = []

for epoch in range(epochs):
    # 模拟训练（实际应包含 optimizer.zero_grad(), loss.backward()）
    optimizer.step()          # 先更新参数
    scheduler.step()          # 再调整学习率（每个 epoch 调用一次）
    lr_list.append(optimizer.param_groups[0]['lr'])

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(range(epochs), lr_list, 'g-', linewidth=2)
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title(f'ExponentialLR (gamma={gamma})')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()