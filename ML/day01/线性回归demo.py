from sklearn.linear_model import LinearRegression


#0.导包
#1.准备数据,使用两层列表的含义，第一层表示有多少条数据组成我们
x_train = [[160],[166],[172],[174],[180]]
# 一般来说，预测值只有一列
y_train = [56.3,60.6,65.1,68.5,75]
x_test = [[176]]
#2.数据预处理（缺失值，异常值等）
#3.特征工程
#4.训练模型
estimator = LinearRegression()
estimator.fit(x_train, y_train)
print(f'斜率和截距：{estimator.coef_},{estimator.intercept_}')
# 模型预测
y_predict = estimator.predict(x_test)
print(f'预测结果：{y_predict}')
#5.模型评估