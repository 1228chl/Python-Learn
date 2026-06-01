import matplotlib
import torch
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False


torch.manual_seed(0)
temperature = torch.randn(30) * 10   # 随机气温

def exp_weighted_avg(data, beta=0.9):
    avg = []
    for i, temp in enumerate(data, 1):
        if i == 1:
            avg.append(temp)
        else:
            new_avg = avg[-1] * beta + (1 - beta) * temp
            avg.append(new_avg)
    return avg

days = torch.arange(1, 31)
plt.scatter(days, temperature, label='原始温度')
plt.plot(days, exp_weighted_avg(temperature, beta=0.5), label='β=0.5')
plt.plot(days, exp_weighted_avg(temperature, beta=0.9), label='β=0.9')
plt.legend()
plt.show()

print(matplotlib.matplotlib_fname())
print(matplotlib.get_cachedir())