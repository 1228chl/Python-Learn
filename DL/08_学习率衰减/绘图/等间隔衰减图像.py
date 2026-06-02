import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 设置参数
initial_lr = 0.1
step_size = 50
gamma = 0.5
epochs = 200

# 创建模型和优化器
model = nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=initial_lr)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=step_size, gamma=gamma)

# 记录学习率变化
lr_list = []
for epoch in range(epochs):
    # 模拟训练步骤（实际应包含完整的前向传播、损失计算、反向传播）
    # loss.backward()
    optimizer.step()        # 正确顺序：先更新参数
    scheduler.step()        # 然后更新学习率
    # 记录当前学习率
    current_lr = optimizer.param_groups[0]['lr']
    lr_list.append(current_lr)

# 绘图
plt.plot(range(epochs), lr_list, linewidth=1)
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title(f'StepLR (step_size={step_size}, gamma={gamma})')
# plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(['Learning Rate'])
plt.show()