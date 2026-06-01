from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

def iris_grid_search_demo():
    # ==================== 1. 加载数据 ====================
    iris = load_iris()
    X = iris.data
    y = iris.target

    # ==================== 2. 划分数据集（训练集+测试集） ====================
    # 注意：测试集在整个调参过程中不能碰，最终只用于评估最优模型
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=22
    )
    print(f"训练集样本数: {X_train.shape[0]}")
    print(f"测试集样本数: {X_test.shape[0]}")

    # ==================== 3. 特征标准化 ====================
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # ==================== 4. 定义基础模型和超参数网格 ====================
    # 基础 KNN 模型（暂时不设 n_neighbors）
    knn = KNeighborsClassifier()

    # 定义要搜索的超参数网格
    param_grid = {
        'n_neighbors': [1, 3, 5, 7, 9, 11],  # K 值候选
        'weights': ['uniform', 'distance'],  # 权重策略
        'p': [1, 2]  # 1:曼哈顿距离，2:欧氏距离
    }

    # ==================== 5. 实例化 GridSearchCV ====================
    # 使用 5 折交叉验证，评分指标为 accuracy，使用所有 CPU 核心
    grid_search = GridSearchCV(
        estimator=knn,  # 要调参的模型
        param_grid=param_grid,  # 超参数网格
        cv=5,  # 5折交叉验证
        scoring='accuracy',  # 评估指标
        n_jobs=-1,  # 并行计算
        verbose=1  # 显示进度
    )

    # ==================== 6. 执行网格搜索 ====================
    # 注意：这里只传入训练集！测试集在调参过程中不参与。
    grid_search.fit(X_train_scaled, y_train)

    # ==================== 7. 查看结果 ====================
    print("\n" + "=" * 50)
    print("网格搜索完成！")
    print("=" * 50)
    print(f"最佳参数组合: {grid_search.best_params_}")
    print(f"最佳交叉验证准确率: {grid_search.best_score_:.4f}")
    print(f"最佳模型: {grid_search.best_estimator_}")

    # 详细结果（转换为 DataFrame 查看）
    cv_results = pd.DataFrame(grid_search.cv_results_)
    # 只显示关键列
    result_cols = ['param_n_neighbors', 'param_weights', 'param_p',
                   'mean_test_score', 'std_test_score', 'rank_test_score']
    print("\n各参数组合的交叉验证结果（前5行）:")
    print(cv_results[result_cols].head())

    # 找出所有组合中 rank_test_score == 1 的（即最佳组合）
    best_rows = cv_results[cv_results['rank_test_score'] == 1]
    print("\n所有最佳参数组合（可能有多个并列）:")
    print(best_rows[result_cols])

    # ==================== 8. 使用最优模型在测试集上评估 ====================
    best_knn = grid_search.best_estimator_
    y_test_pred = best_knn.predict(X_test_scaled)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    print(f"\n最优模型在测试集上的准确率: {test_accuracy:.4f}")
    print("\n测试集分类报告:")
    print(classification_report(y_test, y_test_pred, target_names=iris.target_names))

    # ==================== 9. 对比：如果不调参（默认K=5）的效果 ====================
    default_knn = KNeighborsClassifier()  # n_neighbors=5, weights='uniform', p=2
    default_knn.fit(X_train_scaled, y_train)
    default_pred = default_knn.predict(X_test_scaled)
    default_acc = accuracy_score(y_test, default_pred)
    print(f"\n默认参数模型（K=5, uniform, p=2）测试集准确率: {default_acc:.4f}")

    return grid_search


def plot_k_vs_accuracy(cv_results):
    # 提取 weights='uniform' 且 p=2 的结果
    uniform_p2 = cv_results[(cv_results['param_weights'] == 'uniform') & (cv_results['param_p'] == 2)]
    uniform_p2 = uniform_p2.sort_values('param_n_neighbors')

    plt.figure(figsize=(8, 5))
    plt.plot(uniform_p2['param_n_neighbors'], uniform_p2['mean_test_score'], 'bo-', linewidth=2, markersize=8)
    plt.fill_between(uniform_p2['param_n_neighbors'],
                     uniform_p2['mean_test_score'] - uniform_p2['std_test_score'],
                     uniform_p2['mean_test_score'] + uniform_p2['std_test_score'],
                     alpha=0.2, color='blue')
    plt.xlabel('K值 (n_neighbors)')
    plt.ylabel('交叉验证准确率')
    plt.title('K值对模型准确率的影响 (weights=uniform, p=2)')
    plt.xticks(uniform_p2['param_n_neighbors'])
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


if __name__ == '__main__':
    grid_search = iris_grid_search_demo()
    print(grid_search)
    cv_results = pd.DataFrame(grid_search.cv_results_)
    plot_k_vs_accuracy(cv_results)