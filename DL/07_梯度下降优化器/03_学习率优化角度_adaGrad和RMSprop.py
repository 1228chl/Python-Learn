# 导包
import torch


def test_adagrad():
    # 模拟准备权重数据
    w = torch.tensor([1.0], requires_grad=True)
    # TODO 优化器: Adagrad
    optimizer = torch.optim.Adagrad([w], lr=0.01)
    # 模拟训练迭代n轮
    for i in range(5):
        # todo 如果在循环内计算梯度,它会默认累加,此处需要提前清零
        optimizer.zero_grad()
        # 模拟计算损失
        loss = 0.5 * w ** 2
        # 反向传播计算梯度
        loss.backward()
        print(f"梯度值:{w.grad}")
        # todo 更新参数
        optimizer.step()  # w = w - 0.01 * w.grad
        print(f"更新后的参数:{w}")


def test_rmsprop():
    # 模拟准备权重数据
    w = torch.tensor([1.0], requires_grad=True)
    # TODO 优化器: RMSprop
    optimizer = torch.optim.RMSprop([w], lr=0.01, alpha=0.99)
    # 模拟训练迭代n轮
    for i in range(5):
        # todo 如果在循环内计算梯度,它会默认累加,此处需要提前清零
        optimizer.zero_grad()
        # 模拟计算损失
        loss = 0.5 * w ** 2
        # 反向传播计算梯度
        loss.backward()
        print(f"梯度值:{w.grad}")
        # todo 更新参数
        optimizer.step()  # w = w - 0.01 * w.grad
        print(f"更新后的参数:{w}")


if __name__ == '__main__':
    test_adagrad()
    print('======================================')
    test_rmsprop()
