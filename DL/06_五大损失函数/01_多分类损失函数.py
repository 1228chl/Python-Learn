import torch
import torch.nn as nn

# 示例：3 个样本，4 个类别
logits = torch.tensor([[0.2, 0.6, 0.1, 0.1],
                       [0.8, 0.1, 0.05, 0.05],
                       [0.1, 0.2, 0.5, 0.2]], requires_grad=True)
targets = torch.tensor([1, 0, 2], dtype=torch.int64)  # 真实类别索引

criterion = nn.CrossEntropyLoss()  # reduction='mean' 默认
loss = criterion(logits, targets)
print(loss.item())
print(loss)

targets = torch.tensor([[0, 1, 0],[0,0,1]],dtype=torch.float)
logits = torch.tensor([[2,5,2],[1,2,5]],dtype=torch.float)
loss_fn = torch.nn.CrossEntropyLoss()
print(loss_fn(logits,targets))