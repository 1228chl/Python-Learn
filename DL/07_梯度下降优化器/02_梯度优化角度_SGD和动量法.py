# 导包
import torch

def test_SGD():
    #模拟准备权重数据
    w = torch.tensor([1.0],requires_grad=True)
    # 优化器：SGD
    optimizer = torch.optim.SGD([w],lr=0.01)
    # 模拟训练迭代n轮
    for i in range(10):
        # 如果在循环内计算梯度，它会默认累加，此处需要提前清零
        optimizer.zero_grad()
        print(f"迭代次数：{i}")
        # 模拟计算损失
        loss = 0.5 * w ** 2
        # 反向传播计算梯度
        loss.backward()
        print(f"梯度值：{w.grad}")
        # 更新参数
        # w = w - 0.01 * w.grad
        optimizer.step()
        print(f"更新后的参数：{w}")

def test_SGD_Momentum():
    # 模拟准备权重数据
    w = torch.tensor([1.0], requires_grad=True)
    # 优化器：SGD
    optimizer = torch.optim.SGD([w], lr=0.01, momentum=0.9)
    # 模拟训练迭代n轮
    for i in range(10):
        # 如果在循环内计算梯度，它会默认累加，此处需要提前清零
        optimizer.zero_grad()
        print(f"迭代次数：{i}")
        # 模拟计算损失
        loss = 0.5 * w ** 2
        # 反向传播计算梯度
        loss.backward()
        print(f"梯度值：{w.grad}")
        # 更新参数
        # w = w - 0.01 * w.grad
        optimizer.step()
        print(f"更新后的参数：{w}")

if __name__ == '__main__':
    test_SGD_Momentum()
    test_SGD()