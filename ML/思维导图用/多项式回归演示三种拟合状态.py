import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge, Lasso

# 固定随机种子，保证结果可重复
np.random.seed(666)

# 生成100个在 [-3, 3] 上均匀分布的点
x = np.random.uniform(-3, 3, size=100)
# 真实关系：y = 0.5*x^2 + x + 2，再加上正态分布噪声（标准差=1）
y = 0.5 * x**2 + x + 2 + np.random.normal(0, 1, size=100)

# 将x转换为列向量（sklearn要求特征为二维）
X = x.reshape(-1, 1)

def draw01():
    # 模型1：仅使用原始特征 x（一次项）
    model_under = LinearRegression()
    model_under.fit(X, y)
    y_pred_under = model_under.predict(X)

    # 计算训练误差
    mse_under = mean_squared_error(y, y_pred_under)
    print(f"欠拟合模型训练MSE: {mse_under:.4f}")

    # 绘图
    plt.scatter(x, y, alpha=0.6, label='真实数据')
    plt.plot(np.sort(x), y_pred_under[np.argsort(x)], 'r-', linewidth=2, label='线性拟合 (欠拟合)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('欠拟合示例')
    plt.legend()
    plt.show()

def draw02():
    # 构造新特征：x 和 x^2
    X_poly = np.hstack([X, X ** 2])  # 形状 (100, 2)

    model_good = LinearRegression()
    model_good.fit(X_poly, y)
    y_pred_good = model_good.predict(X_poly)

    mse_good = mean_squared_error(y, y_pred_good)
    print(f"正常拟合模型训练MSE: {mse_good:.4f}")
    print(f"模型系数: {model_good.coef_}, 截距: {model_good.intercept_}")

    # 绘图（因为特征维度2，预测值仍与x对应）
    plt.scatter(x, y, alpha=0.6, label='真实数据')
    idx = np.argsort(x)
    plt.plot(np.sort(x), y_pred_good[idx], 'g-', linewidth=2, label='二次拟合 (正常)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('正常拟合示例')
    plt.legend()
    plt.show()

def draw03():
    # 构造高次特征：x, x^2, x^3, ..., x^10
    X_over = X.copy()
    for degree in range(2, 11):
        X_over = np.hstack([X_over, X ** degree])  # 最终形状 (100, 10)

    model_over = LinearRegression()
    model_over.fit(X_over, y)
    y_pred_over = model_over.predict(X_over)

    mse_over = mean_squared_error(y, y_pred_over)
    print(f"过拟合模型训练MSE: {mse_over:.4f}")

    # 查看高次项系数（绝对值可能非常大）
    print("高次项系数 (x^2~x^10):", model_over.coef_[1:])

    # 绘图
    plt.scatter(x, y, alpha=0.6, label='真实数据')
    # 为了平滑曲线，对 x 排序后画图
    idx = np.argsort(x)
    plt.plot(np.sort(x), y_pred_over[idx], 'm-', linewidth=2, label='10次多项式拟合 (过拟合)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('过拟合示例')
    plt.legend()
    plt.show()

def draw04():
    # 构造高次特征：x, x^2, x^3, ..., x^10
    X_over = X.copy()
    for degree in range(2, 11):
        X_over = np.hstack([X_over, X ** degree])  # 最终形状 (100, 10)

    # Ridge 正则化
    ridge = Ridge(alpha=0.5)
    ridge.fit(X_over, y)
    y_pred_ridge = ridge.predict(X_over)
    print("Ridge 系数 (高次项):", ridge.coef_[1:])
    print("Ridge 训练 MSE:", mean_squared_error(y, y_pred_ridge))

    # 绘图
    plt.scatter(x, y, alpha=0.6, label='真实数据')
    # 为了平滑曲线，对 x 排序后画图
    idx = np.argsort(x)
    plt.plot(np.sort(x), y_pred_ridge[idx], 'm-', linewidth=2, label='10次多项式拟合 (过拟合)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('过拟合示例(Ridge)')
    plt.legend()
    plt.show()

def draw05():
    # 构造高次特征：x, x^2, x^3, ..., x^10
    X_over = X.copy()
    for degree in range(2, 11):
        X_over = np.hstack([X_over, X ** degree])  # 最终形状 (100, 10)

    # Lasso 正则化
    lasso = Lasso(alpha=0.05)
    lasso.fit(X_over, y)
    y_pred_lasso = lasso.predict(X_over)
    print("Lasso 系数 (高次项):", lasso.coef_[1:])
    print("Lasso 训练 MSE:", mean_squared_error(y, y_pred_lasso))

    # 绘图
    plt.scatter(x, y, alpha=0.6, label='真实数据')
    # 为了平滑曲线，对 x 排序后画图
    idx = np.argsort(x)
    plt.plot(np.sort(x), y_pred_lasso[idx], 'm-', linewidth=2, label='10次多项式拟合 (过拟合)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('过拟合示例(Lasso)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # draw01()
    # draw02()
    # draw03()
    # draw04()
    draw05()