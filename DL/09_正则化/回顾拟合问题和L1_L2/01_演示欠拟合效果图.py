# 1.导包
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# 解决FigureCanvasInterAgg问题
import matplotlib

# matplotlib.use('TkAgg')
# 2.准备数据
# 为了保证数据的一致性,这里设置随机数种子
np.random.seed(666)
# 模拟随机生成n维数组
x = np.random.uniform(-3, 3, 100)
print(x, x.shape)
# TODO 注意:加噪声目的是为了让点随机不规则,如果不加就是一个线性关系,加了模拟真实企业的数据
y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)
# 3.创建模型
# TODO 注意: 此处使用的是线性回归模型,只能识别线性关系
model = LinearRegression()
# 4.训练模型
# TODO reshape把(n,)变成了(n,1)列向量,reshape(-1,1)其中的-1代表自动识别大小,1代表一列
X1 = x.reshape(-1, 1)
print(X1, X1.shape)
# # TODO y是二次函数而模型是线性回归(y=kx+b),X1就是一列数据
model.fit(X1, y)
# 5.模型预测
y_predict = model.predict(X1)
# 6.模型评估
print(f'均方误差: {mean_squared_error(y, y_predict)}')  # 均方误差: 3.0750025765636577
# 7.可视化模型拟合效果
plt.scatter(x, y)  # TODO 散点图
plt.plot(x, y_predict, color='red')  # TODO 画出拟合的直线
plt.show()
