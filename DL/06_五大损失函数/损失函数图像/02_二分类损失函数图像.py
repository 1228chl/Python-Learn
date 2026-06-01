import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn

# 设置中文显示（可选）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义预测概率 p 的范围 (0.001 到 0.999 避免 log(0))
p = np.linspace(0.001, 0.999, 500)

# 计算两条损失曲线
loss_y1 = -np.log(p)               # 真实标签 y=1
loss_y0 = -np.log(1 - p)           # 真实标签 y=0

# 用户提供的示例参数
logits = torch.tensor([1.5, 2.5], dtype=torch.float)
targets = torch.tensor([1, 1], dtype=torch.float)
y_pred = torch.sigmoid(logits)     # 预测概率
loss_fn = nn.BCELoss()
loss_value = loss_fn(y_pred, targets).item()

# 提取两个样本的概率和各自的损失（用于标注）
p1, p2 = y_pred[0].item(), y_pred[1].item()
loss1 = -np.log(p1)   # 对应 y=1
loss2 = -np.log(p2)

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制损失曲线
ax.plot(p, loss_y1, 'b-', linewidth=2.5, label=r'真实标签 y=1: $-\log(p)$')
ax.plot(p, loss_y0, 'r-', linewidth=2.5, label=r'真实标签 y=0: $-\log(1-p)$')

# 标注示例点
ax.plot(p1, loss1, 'go', markersize=8, label=f'样本1: p={p1:.3f}, 损失={loss1:.3f}')
ax.plot(p2, loss2, 'co', markersize=8, label=f'样本2: p={p2:.3f}, 损失={loss2:.3f}')
# 添加箭头标注
ax.annotate(f'({p1:.3f}, {loss1:.3f})', xy=(p1, loss1), xytext=(p1+0.1, loss1+0.5),
            arrowprops=dict(arrowstyle='->', color='gray'))
ax.annotate(f'({p2:.3f}, {loss2:.3f})', xy=(p2, loss2), xytext=(p2+0.1, loss2+0.5),
            arrowprops=dict(arrowstyle='->', color='gray'))

# 计算并标注平均损失（BCELoss 默认对 batch 取平均）
ax.annotate(f'Batch 平均损失 = {loss_value:.4f}', xy=(0.6, 4), fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.6))

# 坐标轴设置
ax.set_xlim(0, 1)
ax.set_ylim(0, 8)
ax.set_xlabel('预测概率 $p$', fontsize=12)
ax.set_ylabel('交叉熵损失', fontsize=12)
ax.set_title('二分类交叉熵损失函数曲线', fontsize=14, fontweight='bold')

# 网格和背景
ax.grid(True, linestyle='--', alpha=0.6, linewidth=0.5)
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('white')

# 图例
ax.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()
# 保存图片（可选）
# plt.savefig('binary_cross_entropy.png', dpi=150)