#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: KNN分类和回归.py
作者: ZZS
项目: ml_learn_project
创建日期: 2026/5/25
描述: 
"""

"""
使用knn算法展示如何做分类和回归问题

超参数：邻居的数量，默认是5，n_neighbors = 5

分类问题：和未知样本最近的K个样本的分类，最多的分类就是未知样本的分类。
回归问题：和未知样本最近的K个样本的目标值的平均就是未知样本的目标。

"""

from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor

def demo01_KNN_classification():
    """
    KNN分类
    :return:
    """
    # 1. 获取数据
    x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    # 2. 数据预处理/特征工程，不需要
    # 3. 模型训练
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x,y)
    # 4. 模型预测
    y_predict = estimator.predict([[11]])
    print("预测结果：",y_predict)

def demo02_KNN_regression():
    """
    KNN回归
    :return:
    """
    # 1. 获取数据
    x = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 2. 数据预处理/特征工程，不需要
    # 3. 模型训练
    estimator = KNeighborsRegressor(n_neighbors=3)
    estimator.fit(x,y)
    # 4. 模型预测
    y_predict = estimator.predict([[11, 11]])
    print("预测结果：",y_predict)




if __name__ == '__main__':
    # demo01_KNN_classification()
    demo02_KNN_regression()



