#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: 演示kmeans算法.py
作者: ZZS
项目: ml_learn_project
创建日期: 2026/5/26
描述: 
"""

"""
需求：使用 make_blobs 生成2维多条数据，然后使用kmeans对数据进行聚类。

"""
import os
import sys
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score           # 轮廓系数
from sklearn.metrics import calinski_harabasz_score    # CH指数
import numpy as np
import pandas as pd

def demo01_kmeans_cluster():
    """
    使用kmeans对数据进行聚类
    :return:
    """
    # 1. 生成数据
    x,y = make_blobs(n_samples=1000,n_features=2,centers=[[-1,-1],[0,0],[1,1],[2,2]],
                     cluster_std = [0.4,0.2,0.2,0.2], random_state=42)
    # 画图
    plt.scatter(x[:,0],x[:,1])
    plt.show()

    # 2. 模型训练
    # 2.1 分成两簇
    estimator = KMeans(n_clusters=2)
    estimator.fit(x)
    # 预测
    y_predict = estimator.predict(x)
    # 画图
    plt.scatter(x[:,0],x[:,1],c=y_predict)
    plt.show()

    # 2.2 分成三簇
    estimator = KMeans(n_clusters=3)
    estimator.fit_predict(x)
    # 预测
    y_predict = estimator.predict(x)
    # 画图
    plt.scatter(x[:, 0], x[:, 1], c=y_predict)
    plt.show()

    # 2.3 分成四簇
    estimator = KMeans(n_clusters=4)
    estimator.fit_predict(x)
    # 预测
    y_predict = estimator.predict(x)
    # 画图
    plt.scatter(x[:, 0], x[:, 1], c=y_predict)
    plt.show()

    # 3 模型评估
    print("SSE",estimator.inertia_)                      # SSE，误差平方和，范围：[0,无穷大]
    print("轮廓系数",silhouette_score(x,y_predict))        # 轮廓系数 范围：[-1,1]
    print("CH指数",calinski_harabasz_score(x,y_predict))  # CH指数，范围：[0,无穷大]，基本不用

#



if __name__ == '__main__':
    demo01_kmeans_cluster()
