import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示（可选）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义预测值范围
y_pred = np.linspace(-3, 3, 500)

# 定义真实值（可修改）
y_true = 0

# MSE 损失: (y_pred - y_true)^2
mse_loss = (y_pred - y_true) ** 2

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(y_pred, mse_loss, 'b-', linewidth=2.5, label=r'MSE Loss: $(y - \hat{y})^2$')

# 标注最低点（预测等于真实值）
ax.plot(y_true, 0, 'ro', markersize=8, label=f'最小值点 (y_true = {y_true})')

# 坐标轴设置
ax.set_xlabel(r'预测值 $\hat{y}$', fontsize=12)
ax.set_ylabel('MSE 损失', fontsize=12)
ax.set_title('均方误差 (MSE) 损失函数曲线', fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('white')
ax.legend(loc='upper center', fontsize=10)

plt.tight_layout()
plt.show()
# 保存图片（可选）
# plt.savefig('mse_loss.png', dpi=150)