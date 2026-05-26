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
使用肘方法，收集从1~100的聚类中心数训练出来的kmeans模型对应sse，画图看拐点。

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

    # 2. 模型训练，从1到100的kmeans模型，对应sse，放到sse_list里
    sse_list = []
    for k in range(1,100):
        estimator = KMeans(n_clusters=k)
        y_predict = estimator.fit_predict(x)
        sse_list.append(estimator.inertia_)    # 将模型的sse 误差平方和的指标放到sse_list里。

    # 3. 用sse列表画图
    plt.figure(figsize=(18,8),dpi=100)
    # 坐标轴使用0~100，每隔3个数展示
    plt.xticks(range(0,100,1))
    plt.grid()
    plt.title("SSE")
    plt.plot(range(1,100),sse_list)
    plt.show()




if __name__ == '__main__':
    demo01_kmeans_cluster()
