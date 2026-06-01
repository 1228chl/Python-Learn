import torch

targets = torch.tensor([1, 1],dtype=torch.float)
logits = torch.tensor([1.5, 2.5],dtype=torch.float)
y_pred = torch.sigmoid(logits)
loss_fn = torch.nn.BCELoss()
print(loss_fn(y_pred,targets))