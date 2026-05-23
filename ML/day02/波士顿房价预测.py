# 导入必要的库
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error
import numpy as np
import pandas as pd

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

print("测试集：",data)
print("目标：",target)
print("测试集长度：",len(data))

def demo01_linear_regression():
    X_train,X_test,Y_train,Y_test = train_test_split(data,target,test_size=0.2,random_state=42)

    print("标准化之前测试集：",X_test)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    print("标准化之后测试集：",X_test)

    estimator = LinearRegression()
    estimator.fit(X_train, Y_train)

    Y_predict = estimator.predict(X_test)

    mse = mean_squared_error(Y_test, Y_predict)
    print(mse)
    mae = mean_absolute_error(Y_test, Y_predict)
    print(mae)
    rmse = root_mean_squared_error(Y_test, Y_predict)
    print(rmse)

def demo02_sgd_regression():
    X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size=0.2, random_state=42)

    print("标准化之前测试集：", X_test)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    print("标准化之后测试集：", X_test)

    # estimator = LinearRegression()
    estimator = SGDRegressor()

    estimator.fit(X_train, Y_train)

    Y_predict = estimator.predict(X_test)

    mse = mean_squared_error(Y_test, Y_predict)
    print(mse)
    mae = mean_absolute_error(Y_test, Y_predict)
    print(mae)
    rmse = root_mean_squared_error(Y_test, Y_predict)
    print(rmse)

if __name__ == '__main__':
    time = datetime.now()
    demo01_linear_regression()
    print("运行时间：", datetime.now() - time)
    demo02_sgd_regression()
    print("运行时间：", datetime.now() - time)
