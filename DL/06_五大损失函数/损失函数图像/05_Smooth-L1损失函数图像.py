import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

def smooth_l1_loss(x):
    loss = np.where(np.abs(x) < 1, 0.5 * x ** 2, np.abs(x) - 0.5)
    return loss

# 定义差值范围
x = np.linspace(-3, 3, 500)
loss = smooth_l1_loss(x)

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, loss, 'purple', linewidth=2.5, label='Smooth L1 Loss')

# 标注分段点 x = ±1
for x0 in [-1, 1]:
    y0 = smooth_l1_loss(x0)
    ax.plot(x0, y0, 'ro', markersize=6)
    ax.annotate(f'$x={x0}$', xy=(x0, y0), xytext=(x0+0.2, y0+0.2),
                arrowprops=dict(arrowstyle='->', color='gray'))

# 使用原始字符串（r''）避免转义问题
ax.text(1.5, 2.2, r'Smooth L1 定义：', fontsize=11, bbox=dict(facecolor='white', alpha=0.8))
ax.text(1.5, 1.8, r'$|x| < 1$ 时: $0.5x^2$', fontsize=10)
ax.text(1.5, 1.4, r'$|x| \geq 1$ 时: $|x| - 0.5$', fontsize=10)

# 坐标轴设置（使用原始字符串）
ax.set_xlabel(r'差值 $x = y - \hat{y}$', fontsize=12)
ax.set_ylabel('损失', fontsize=12)
ax.set_title('Smooth L1 损失函数曲线', fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('white')
ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()