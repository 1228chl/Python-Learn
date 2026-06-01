import torch

# 创建一个标量张量，开启梯度追踪
x = torch.tensor(3.0,requires_grad=True)
# 定义一个函数 y=x^2
y = (x ** 2)**2
# 反向传播（因为y是标量，直接调用）
y.backward()
# 打印梯度 dy/dx = 2*x = 6.0
print(x.grad)

