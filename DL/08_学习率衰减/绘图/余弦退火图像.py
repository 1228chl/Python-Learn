import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 创建模型和优化器
model = nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# 创建 CosineAnnealingLR 调度器
T_max = 100          # 周期长度
eta_min = 0          # 最小学习率
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=T_max, eta_min=eta_min)

epochs = 200
lr_list = []

for epoch in range(epochs):
    optimizer.step()          # 先更新参数
    scheduler.step()          # 再调整学习率
    lr_list.append(optimizer.param_groups[0]['lr'])

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(range(epochs), lr_list, 'r-', linewidth=2)
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title(f'CosineAnnealingLR (T_max={T_max}, eta_min={eta_min})')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()