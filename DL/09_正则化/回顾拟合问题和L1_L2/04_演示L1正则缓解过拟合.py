# 1.导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error
# 解决FigureCanvasInterAgg问题
import matplotlib
# matplotlib.use('TkAgg')
# 2.准备数据
# 为了保证数据的一致性,这里设置随机数种子
np.random.seed(666)
# 模拟随机生成n维数组
x = np.random.uniform(-3, 3, 100)
# TODO 注意: 此处噪声你可以尝试去掉,观察最终效果(原始数据和预测数据重合为一条曲线)
# 建议加上噪声,模拟真实企业数据,不可能完全拟合,因为真实企业数据一般不会完全符合线性关系
y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, 100)
# 3.创建模型
# model = LinearRegression()
model = Lasso(alpha=0.1)
# 4.训练模型
X1 = x.reshape(-1, 1)
# TODO y是二次函数而模型转换后X2也包含了X1的平方(二次项),最终训练X2,可以解决欠拟合问题达到正好拟合效果
X2 = np.hstack([X1, X1 ** 2, X1 ** 3, X1 ** 4, X1 ** 5, X1 ** 6, X1 ** 7, X1 ** 8, X1 ** 9, X1 ** 10,
                X1 ** 11, X1 ** 12, X1 ** 13, X1 ** 14, X1 ** 15, X1 ** 16, X1 ** 17, X1 ** 18, X1 ** 19, X1 ** 20,
                X1 ** 21, X1 ** 22, X1 ** 23, X1 ** 24])
model.fit(X2, y)
# 5.模型预测
y_predict = model.predict(X2)
# 6.模型评估
print(f'均方误差: {mean_squared_error(y, y_predict)}')  # 均方误差: 1.0987392142417856
# 7.可视化模型拟合效果
plt.scatter(x, y)
# TODO np.sort(x) : 升序排列x
# TODO np.argsort(x): 拿到x排序后的索引,再通过索引拿到y_predict的值
# TODO y_predict[np.argsort(x)] : 根据x所以找到对应的y_predict值
plt.plot(np.sort(x), y_predict[np.argsort(x)], color='red')
plt.show()
