#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: KNN分类鸢尾花.py
作者: ZZS
项目: ml_learn_project
创建日期: 2026/5/25
描述: 
"""
from day01.线性回归demo import y_predict

"""
需求：使用KNN实现对鸢尾花的分类。
    包括数据集的下载，查看，数据的画图展示，数据切分，特征工程（标准化），模型训练，预测，评估。
    
"""
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris



def demo01_KNN_classification():
    """
    KNN分类
    :return:
    """
    # 1. 数据准备
    iris = load_iris()
    # 查看数据
    print("数据集的描述：",iris.DESCR)
    print("数据集的标签：",iris.target_names)
    print("数据集的特征：",iris.feature_names)
    print("数据集的大小：",iris.data.shape)
    print("数据集的标签：",iris.target.shape)
    print("数据集：",iris.data[:5])
    print("数据集的标签：",iris.target[:5])

    # 1.1 可视化
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['label'] = iris.target
    print(df)
    sns.lmplot(x="petal length (cm)",y="petal width (cm)",hue="label",data=df,fit_reg=False)
    plt.xlabel = "petal length (cm)"
    plt.ylabel = "petal width (cm)"
    plt.title = "iris"
    plt.show()

    # 切分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=44)
    # 2. 数据预处理（缺失值，异常），没有

    # 3. 特征工程（标准化）
    ss = StandardScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)

    # 看一下转换后的测试集的数据
    print("标准化之后的数据集：",x_train)

    # 4. 模型训练
    estimator = KNeighborsClassifier(n_neighbors=2)
    estimator.fit(x_train,y_train)
    # 5. 模型预测
    y_predict = estimator.predict(x_test)
    print("测试集的特征：",x_test)
    print("真实结果：",y_test)
    print("预测结果：",y_predict)
    # 6. 模型评估
    print("准确率：",estimator.score(x_test,y_test))
    print("准确率：",accuracy_score(y_test,y_predict))
    print("精确率：",precision_score(y_test,y_predict,average='macro'))
    print("召回率：",recall_score(y_test,y_predict,average='macro'))
    print("F1-score：",f1_score(y_test,y_predict,average='macro'))
    print("混淆矩阵：",confusion_matrix(y_test,y_predict))




if __name__ == '__main__':
    demo01_KNN_classification()


