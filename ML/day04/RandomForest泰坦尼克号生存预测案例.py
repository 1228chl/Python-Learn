#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: RandomForest泰坦尼克号生存预测案例.py
作者: ZZS
项目: ml_learn_project
创建日期: 2026/5/25
描述: 
"""
"""
需求：
 1 使用cart决策树对泰坦尼克号数据进行训练，并评估，预测，以及画图。
 2 使用随机森林对泰坦尼克号数据进行训练，并评估，预测
 3 使用交叉验证和网格搜索，将随机森林作为基学习器，对泰坦尼克号数据进行训练，并评估，预测


使用的是cart决策树的分类能力，标签是 died or survived。
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, recall_score,f1_score,accuracy_score,precision_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def demo01_cart_classification():
    """
    CART决策树做分类
    :return:
    """
    # 1. 数据准备
    df = pd.read_csv("./train.csv")
    df.info()

    # 2. 数据预处理，拿取特征和标签
    x = df[["Pclass","Sex","Age"]]
    x = x.copy()
    y = df["Survived"]
    # print(y)

    # 2.1 年龄填充，因为有缺失
    x["Age"] = x.Age.fillna(x.Age.mean(),inplace=True)
    print("独热编码之前的数据")
    x.info()
    # 2.2 对性别字段做独热编码
    x = pd.get_dummies(x,columns=["Sex"])
    print("独热编码之后的数据")
    x.info()

    # 2.3 数据集切分
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    # 3. 模型训练
    # 3.1 实例化模型
    estimator = DecisionTreeClassifier()
    # 3.2 训练模型
    estimator.fit(x_train,y_train)
    # 4. 模型预测
    y_predict = estimator.predict(x_test)
    # 5. 模型评估
    # 5.1 使用准确率
    print("CART树的准确率：",accuracy_score(y_test,y_predict))
    # 5.2 使用更加详细分类的报告 classification_report
    # print(classification_report(y_test,y_predict))


    # 7. 使用随机森林做分类和预测评估
    RFC = RandomForestClassifier(n_estimators=10, max_depth = 5, random_state = 42)
    RFC.fit(x_train,y_train)
    y_predict = RFC.predict(x_test)
    print("随机森林准确率：",accuracy_score(y_test,y_predict))

    # 8. 使用交叉验证和网格搜索
    param_grid = {"n_estimators": [10, 20, 30, 40, 50],"max_depth":[5,10,15,20],"random_state": [42]}
    GSC = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_grid, cv=2)
    GSC.fit(x_train,y_train)
    # 预测
    y_predict = GSC.predict(x_test)
    print("交叉验证和网格搜索的准确率：",GSC.best_score_)
    print("模型测试集准确率：",accuracy_score(y_test,y_predict))
    print("交叉验证和网格搜索的模型：",GSC.best_estimator_)


    # 6. 画图
    # plt.figure(figsize=(100,100))
    # plot_tree(estimator,
    #            max_depth=30,
    #            filled=True,
    #            feature_names=['Pclass', 'Age', 'Sex_female', 'Sex_male'],
    #            class_names=['died', 'survived']
    #            )
    # plt.show()




if __name__ == '__main__':
    demo01_cart_classification()


