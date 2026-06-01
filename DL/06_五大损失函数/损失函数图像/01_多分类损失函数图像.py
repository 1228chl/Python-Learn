import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# # 数据定义
# classes = ['类别 0', '类别 1', '类别 2']
# true_onehot = np.array([0, 1, 0])      # 真实标签 (one-hot)
# pred_probs = np.array([0.10, 0.70, 0.20])  # 模型预测概率
#
# # 计算交叉熵损失
# correct_prob = pred_probs[1]  # 真实类别索引为 1
# loss = -np.log(correct_prob)
#
# # 创建图形
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
#
# # 子图1：真实分布 vs 预测概率
# x = np.arange(len(classes))
# width = 0.35
# ax1.bar(x - width/2, true_onehot, width, label='真实分布 (one-hot)', color='tab:blue')
# ax1.bar(x + width/2, pred_probs, width, label='预测概率', color='tab:orange')
# ax1.set_xticks(x)
# ax1.set_xticklabels(classes)
# ax1.set_ylabel('概率')
# ax1.set_title('真实标签 vs 预测概率')
# ax1.legend()
#
# # 在正确类别上添加数值标注
# ax1.annotate(f'正确类概率 = {correct_prob:.2f}', xy=(1, correct_prob), xytext=(1, correct_prob+0.05),
#              ha='center', fontsize=10, color='red')
#
# # 子图2：展示交叉熵损失的计算
# ax2.bar(['正确类概率 (p=0.70)'], [correct_prob], color='green', alpha=0.7)
# ax2.set_ylabel('概率')
# ax2.set_title(f'交叉熵损失 = -log(p) = -log({correct_prob:.2f}) = {loss:.4f}')
# ax2.set_ylim(0, 1)
# # 添加辅助线表示损失含义
# ax2.annotate(f'损失 = {loss:.4f}', xy=(0, correct_prob), xytext=(0.2, correct_prob-0.1),
#              arrowprops=dict(arrowstyle='->'), fontsize=12)
#
# # 添加总标题
# plt.suptitle('多分类交叉熵损失示例', fontsize=14)
# plt.tight_layout()
# plt.show()

# 设置 matplotlib 支持中文（避免标题乱码）

# 生成预测概率 p 从 0.001 到 1.0 的连续点
p = np.linspace(0.001, 1.0, 500)
# 交叉熵损失（自然对数），也可用 np.log10 以常用对数为底
loss = -np.log(p)          # 自然对数
# loss = -np.log10(p)      # 常用对数（值会更小，可自行调整）

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制曲线
ax.plot(p, loss, linewidth=2.5, color='#1f77b4', label=r'交叉熵损失 $L(p) = -\ln(p)$')

# 添加参考点：p=0.7, loss=-ln(0.7)≈0.3567
p0 = 0.7
loss0 = -np.log(p0)
ax.plot(p0, loss0, 'ro', markersize=8, label=f'p={p0}, loss={loss0:.3f}')
ax.annotate(f'({p0}, {loss0:.3f})', xy=(p0, loss0), xytext=(p0+0.05, loss0+0.5),
            arrowprops=dict(arrowstyle='->', color='gray'))

# 设置坐标轴范围
ax.set_xlim(0, 1)
ax.set_ylim(0, max(loss) * 1.05)  # 让 y 轴上限略高于最大损失
# 若希望 y 轴最大为 10（类似你图片中的 9.20），可手动设定：
# ax.set_ylim(0, 10)

# 坐标轴标签与标题
ax.set_xlabel('正确类别的预测概率 $p$', fontsize=12)
ax.set_ylabel('交叉熵损失 $L$', fontsize=12)
ax.set_title('交叉熵损失函数曲线', fontsize=14, fontweight='bold')

# 添加网格（样式可调）
ax.grid(True, linestyle='--', alpha=0.6, linewidth=0.5)
ax.set_axisbelow(True)   # 网格置于底层

# 可选：添加背景颜色填充（类似图片中的淡灰背景）
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('white')

# 图例
ax.legend(loc='upper right', fontsize=10)

# 显示或保存图片
plt.tight_layout()
plt.show()
# plt.savefig('cross_entropy_curve.png', dpi=150)