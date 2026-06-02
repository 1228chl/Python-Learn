# 导包
import torch
# TODO 1.模拟准备数据
x = torch.randint(1,10,size=(1,4),dtype=torch.float)
print(f'输入数据:{x}')

# TODO 2.创建全连接层并处理数据
fc = torch.nn.Linear(4,5)
x = fc(x)
print(f'全连接层处理后数据:{x}')

# TODO 3.随机失活层一般都在全连接层之后
dropout = torch.nn.Dropout(p=0.4)
out = dropout(x)
print(f"随机失活后数据:{out}")