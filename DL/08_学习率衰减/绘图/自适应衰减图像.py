import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# 创建模拟模型和优化器
model = nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# 创建 ReduceLROnPlateau 调度器
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer,
    mode='min',
    factor=0.5,
    patience=10,
    threshold=0.001,
    cooldown=0, 
    min_lr=1e-6
    # 注意：这里移除了 verbose 参数，代码现在可以正常运行了
)

# 模拟验证损失（epoch, loss）
epochs = 100
# 构造损失曲线：前30下降，中30缓慢下降，后40平坦+噪声
np.random.seed(42)
losses = []
for e in range(epochs):
    if e < 30:
        loss = 0.8 * np.exp(-0.1 * e) + 0.1
    elif e < 60:
        loss = 0.05 * np.exp(-0.03 * (e - 30)) + 0.03
    else:
        loss = 0.02 + 0.005 * np.random.randn()
    losses.append(loss)

# 记录学习率变化
lr_history = []
loss_history = []

for epoch in range(epochs):
    # 当前学习率
    current_lr = optimizer.param_groups[0]['lr']
    lr_history.append(current_lr)
    loss_history.append(losses[epoch])

    # 模拟训练步骤（这里省略前向/反向，直接用模拟损失）
    # optimizer.step()  # 实际训练中需要
    # 重要：scheduler.step() 需要传入验证损失
    scheduler.step(losses[epoch])

# 绘图：双纵轴
fig, ax1 = plt.subplots(figsize=(12, 6))

# 左轴：验证损失
color = 'tab:blue'
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Validation Loss', color=color, fontsize=12)
ax1.plot(range(epochs), loss_history, color=color, linewidth=2, label='Validation Loss')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

# 右轴：学习率
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Learning Rate', color=color, fontsize=12)
ax2.plot(range(epochs), lr_history, color=color, linewidth=2, linestyle='--', label='Learning Rate')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

# 标注学习率衰减点（寻找学习率变化的 epoch）
lr_array = np.array(lr_history)
change_epochs = np.where(np.diff(lr_array) < 0)[0] + 1
for ep in change_epochs:
    ax1.axvline(x=ep, color='gray', linestyle=':', alpha=0.7)
    ax1.text(ep + 1, ax1.get_ylim()[1] * 0.9, f'衰减\n(×{scheduler.factor})',
             fontsize=8, ha='center')

plt.title('ReduceLROnPlateau 自适应衰减 (监控验证损失)', fontsize=14)
plt.tight_layout()
plt.show()