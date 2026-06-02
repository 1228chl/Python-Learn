import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 创建模型和优化器
model = nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
milestones = [50, 125, 160]
gamma = 0.1
scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=milestones, gamma=gamma)

epochs = 200
lr_list = []

for epoch in range(epochs):
    # 模拟训练（实际应包含 optimizer.zero_grad(), loss.backward()）
    optimizer.step()          # 先更新参数
    scheduler.step()          # 再调整学习率
    lr_list.append(optimizer.param_groups[0]['lr'])

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(range(epochs), lr_list, 'b-', linewidth=2, drawstyle='steps-post')
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title(f'MultiStepLR (milestones={milestones}, gamma={gamma})')
plt.grid(True, linestyle='--', alpha=0.6)

# 标注衰减点
for m in milestones:
    plt.axvline(x=m, color='gray', linestyle=':', alpha=0.7)

plt.show()