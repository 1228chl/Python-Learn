#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: CART决策树泰坦尼克号生存预测案例.py
作者: ZZS
项目: ml_learn_project
创建日期: 2026/5/25
描述: 
"""
from day01.线性回归demo import y_predict

"""
需求：使用cart决策树对泰坦尼克号数据进行训练，并评估，预测，以及画图。

使用的是cart决策树的分类能力，标签是 died or survived。
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,recall_score,f1_score,accuracy_score,precision_score
import matplotlib.pyplot as plt
import matplotlib
from sklearn.tree import plot_tree

def demo01_cart_classification():
    """
    CART决策树做分类
    :return:
    """
    #1. 数据准备
    df = pd.read_csv("./data/train.csv")
    df.info()
    #2. 数据预处理，拿取特征和标签
    x = df[["Pclass","Sex","Age"]].copy()
    y = df["Survived"]
    #2.1 年龄填充，因为有缺失
    x["Age"] = x["Age"].fillna(x["Age"].mean())
    x.info()
    #2.2 对性别字段做独热编码
    x = pd.get_dummies(x,columns=["Sex"])
    print("独热编码之后的数据")
    x.info()
    #2.3 数据集切分
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    #3.模型训练
    #3.1 实例化模型
    estimator = DecisionTreeClassifier()
    #3.2 训练模型
    estimator.fit(x_train,y_train)
    #4. 模型预测
    y_predict = estimator.predict(x_test)
    #5. 模型评估
    #5.1 使用准确率
    print("准确率：",accuracy_score(y_test,y_predict))
    #5.2 使用更加详细分类的报告 classification_report
    print(classification_report(y_test,y_predict))
    #6. 画图
    plt.figure(figsize=(100,100))
    plot_tree(
        estimator,
        max_depth=30,
        filled=True,               # 节点填充颜色（类别不同颜色不同）
        feature_names=['Pclass', 'Age', 'Sex_female', 'Sex_male'],
        class_names=['died', 'survived'])
    plt.savefig('tree.png',dpi=300,bbox_inches='tight')
    import os
    os.startfile('tree.png')

if __name__ == '__main__':
    demo01_cart_classification()
