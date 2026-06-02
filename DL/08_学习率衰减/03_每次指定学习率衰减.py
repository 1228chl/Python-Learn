# 导包
import torch
import matplotlib.pyplot as plt

# 提前准备优化器
w = torch.tensor([1.0], requires_grad=True)
optimizer = torch.optim.SGD([w],lr=0.1,momentum=0.9)
# 创建学习率衰减对象
lr_scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.5)
# 模拟训练轮次200轮
epochs = 200
# 提前定义两个空列表，存储轮次和学习率，目的是后续画图
epochs_list,lr_list = [],[]
for epoch in range(epochs):
    print(f"当前学习率为：{lr_scheduler.get_last_lr()}")
    epochs_list.append(epoch)
    lr_list.append(lr_scheduler.get_last_lr()[0])
    # 理论上应该拿着当前学习率去反向传播更新参数 -> 新参数 = 旧参数 - 当前学习率 * 梯度
    # 学习率每更新完参数后，衰减一次
    lr_scheduler.step() # 当前学习率 = 旧学习率 * gamma

# 最后画图，x轴轮次，y轴学习率
plt.plot(epochs_list,lr_list)
plt.show()
