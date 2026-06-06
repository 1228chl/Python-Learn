import torch
print(torch.cuda.is_available())   # 应输出 True
print(torch.cuda.get_device_name(0))  # 应显示 GeForce RTX 2060