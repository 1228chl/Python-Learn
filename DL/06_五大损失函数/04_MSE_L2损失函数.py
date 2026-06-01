# 导包
import torch
# 模拟准备真实回归数据，假设房价
y_true = torch.tensor([10,20,30,40],dtype=torch.float)
# 模拟模型的预测结果
y_pred = torch.tensor([9.5,23.5,29.9,41],dtype=torch.float)
# 创建损失函数
loss_fn = torch.nn.MSELoss()
# 计算损失
loss = loss_fn(y_pred,y_true)
print(loss)