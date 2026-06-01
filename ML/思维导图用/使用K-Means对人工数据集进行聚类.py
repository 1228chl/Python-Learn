# 1. 导入工具包
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import calinski_harabasz_score

# 2. 创建数据集：1000个样本，每个样本2个特征，4个中心点，簇标准差不同
x, y = make_blobs(
    n_samples=1000,
    n_features=2,
    centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
    cluster_std=[0.4, 0.2, 0.2, 0.2],
    random_state=22
)

# 3. 可视化原始数据
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(x[:, 0], x[:, 1], marker='o')
plt.title("原始数据")

# 4. 使用 K-Means 进行聚类（设定簇数为3，实际有4个簇，故意调低观察效果）
y_pred = KMeans(n_clusters=3, random_state=22).fit_predict(x)

# 5. 可视化聚类结果
plt.subplot(1, 2, 2)
plt.scatter(x[:, 0], x[:, 1], c=y_pred, cmap='viridis')
plt.title("K-Means 聚类结果 (n_clusters=3)")
plt.show()

# 6. 评估聚类效果（Calinski-Harabasz 指数，后面详细介绍）
ch_score = calinski_harabasz_score(x, y_pred)
print(f"Calinski-Harabasz 指数: {ch_score:.2f}")