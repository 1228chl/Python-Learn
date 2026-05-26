from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt


def evaluate_best_knn():
    #1.加载数据
    iris = load_iris()
    x,y = iris.data,iris.target
    target_names = iris.target_names
    #2.划分+标准化
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=22)
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    #3.网格搜索（简化版）
    param_grid = {'n_neighbors':[1,3,5,7,9,11]}
    knn = KNeighborsClassifier()
    gs = GridSearchCV(knn,param_grid,cv=5,scoring='accuracy',n_jobs=-1)
    gs.fit(x_train_scaled,y_train)
    best_knn = gs.best_estimator_
    print(f"最佳K值：{gs.best_params_['n_neighbors']}")
    #4.预测测试集
    y_pred = best_knn.predict(x_test_scaled)
    #5.评估指标
    print("\n"+"="*50)
    print("测试集评估报告")
    print("=="*25)
    print(f"准确率：{accuracy_score(y_pred,y_test):.4f}")
    print("\n分类报告（包含精确率/召回率/F1）：")
    print(classification_report(y_test,y_pred,target_names=target_names))
    #6.混淆矩阵可视化
    cm = confusion_matrix(y_test,y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm,annot=True,fmt='d',cmap='Blues',xticklabels=target_names,yticklabels=target_names)
    plt.xlabel("预测类别")
    plt.ylabel("真实类别")
    plt.title('混淆矩阵')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    evaluate_best_knn()
