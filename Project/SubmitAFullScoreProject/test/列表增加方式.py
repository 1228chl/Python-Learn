import torch
train_trues = []
# 模拟有一批结果
label1 = [2, 3, 3, 3]
label1 = torch.tensor(label1)
label2 = [2, 3, 9, 7]
label2 = torch.tensor(label2)
# 添加到总列表中
train_trues.extend(label1.tolist())
train_trues.extend(label2.tolist())
print(train_trues)



