#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: 模型拟合情况.py
作者: ZZS
项目: ml_learn_project
创建日期: 2026/5/23
描述: 
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from unicodedata import normalize

from day02.波士顿房价预测 import demo02_sgd_regression


def deme01_模型欠拟合():
    """
    欠拟合
    :return:
    """
    # 1. 准备数据
    np.random.seed(666)
    x = np.random.uniform(-3.0, 3.0, size=100)
    y = 0.5 * x**2 + x + 2 + np.random.normal(size=100)

    # 将[1.20262273  2.06511986  1.05908602...] 转成 [[ 1.20262273] [ 2.06511986] [ 1.05908602]。。。]
    print(x)
    X = x.reshape(-1,1)
    print(X)

    # 2 模型训练
    estimator = LinearRegression()
    estimator.fit(X,y)
    print(estimator.coef_)
    print(estimator.intercept_)

    # 3 模型预测
    y_predict = estimator.predict(X)

    # 4 模型评估, MSE
    mse = mean_squared_error(y,y_predict)

    # 5 画图
    plt.scatter(x,y)
    plt.plot(x,y_predict)
    plt.show()

def demo2_模型正常():
    """
    模型正好拟合的情况
    :return:
    """
    # 1. 准备数据
    np.random.seed(666)
    x = np.random.uniform(-3.0, 3.0, size=100)
    y = 0.5 * x**2 + x + 2 + np.random.normal(size=100)
    X = x.reshape(-1,1)
    # 增加一个x的二次项，相当于增加了模型的复杂读
    X = np.hstack([X, X ** 2])  # 数据增加二次项
    print(X)
    # 2. 模型训练
    estimator = LinearRegression()
    estimator.fit(X,y)
    print(estimator.coef_)
    print(estimator.intercept_)
    # 3. 模型预测
    y_predict = estimator.predict(X)
    # 4. 模型评估, MSE
    mse = mean_squared_error(y,y_predict)
    print(mse)
    # 5. 画图
    plt.scatter(x,y)
    # plt.plot(x,y_predict)
    # 画图plot折线图时 需要对x进行排序, 取x排序后对应的y值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()

def demo3_模型过拟合():
    # 1. 准备数据
    np.random.seed(666)
    x = np.random.uniform(-3.0, 3.0, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(size=100)
    X = x.reshape(-1, 1)
    # 增加一个x的二次项，相当于增加了模型的复杂读
    X = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])  # 数据增加二次项
    print(X)
    # 2. 模型训练
    estimator = LinearRegression()
    estimator.fit(X, y)
    print(estimator.coef_)
    print(estimator.intercept_)
    # 3. 模型预测
    y_predict = estimator.predict(X)
    # 4. 模型评估, MSE
    mse = mean_squared_error(y, y_predict)
    print(mse)
    # 5. 画图
    plt.scatter(x, y)
    # plt.plot(x,y_predict)
    # 画图plot折线图时 需要对x进行排序, 取x排序后对应的y值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()

def demo4_模型过拟合_解决方法_L1():
    """
    模型过拟合解决办法之L1正则
    :return:
    """

    # 1. 准备数据
    np.random.seed(666)
    x = np.random.uniform(-3.0, 3.0, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(size=100)
    X = x.reshape(-1, 1)
    # 增加一个x的二次项，相当于增加了模型的复杂读
    X = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])  # 数据增加二次项
    print(X)
    # 2. 模型训练
    estimator = Lasso(alpha=0.005)
    estimator.fit(X, y)
    print(estimator.coef_)
    print(estimator.intercept_)
    # 3. 模型预测
    y_predict = estimator.predict(X)
    # 4. 模型评估, MSE
    mse = mean_squared_error(y, y_predict)
    print(mse)
    # 5. 画图
    plt.scatter(x, y)
    # plt.plot(x,y_predict)
    # 画图plot折线图时 需要对x进行排序, 取x排序后对应的y值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()

def demo5_模型过拟合_解决方法_L2():
    """
    过拟合解决模型，L2正则
    :return:
    """
    # 1. 准备数据
    np.random.seed(666)
    x = np.random.uniform(-3.0, 3.0, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(size=100)
    X = x.reshape(-1, 1)
    # 增加一个x的二次项，相当于增加了模型的复杂读
    X = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])  # 数据增加二次项
    print(X)
    # 2. 模型训练
    estimator = Ridge(alpha=0.1)
    estimator.fit(X, y)
    print(estimator.coef_)
    print(estimator.intercept_)
    # 3. 模型预测
    y_predict = estimator.predict(X)
    # 4. 模型评估, MSE
    mse = mean_squared_error(y, y_predict)
    print(mse)
    # 5. 画图
    plt.scatter(x, y)
    # plt.plot(x,y_predict)
    # 画图plot折线图时 需要对x进行排序, 取x排序后对应的y值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()

if __name__ == '__main__':
    # deme01_模型欠拟合()
    # demo2_模型正常()
    # demo3_模型过拟合()
    # demo4_模型过拟合_解决方法_L1()
    demo5_模型过拟合_解决方法_L2()