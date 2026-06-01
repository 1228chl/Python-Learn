import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. 读取数据
dataset = pd.read_csv('./data/customers.csv')

# 2. 选择用于聚类的特征（年收入和消费指数）
X = dataset.iloc[:, [3, 4]]   # 假设第4列是年收入，第5列是消费指数

# 3. 使用肘方法确定最佳K值（可选，此处直接设定K=5）
# 根据业务经验和肘方法，选择5个簇

# 4. 训练K-Means模型
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# 5. 预测簇标签
y_kmeans = kmeans.predict(X)

# 6. 可视化聚类结果
plt.figure(figsize=(10, 7))

# 分别绘制每个簇的散点图（使用不同颜色）
colors = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = ['Standard', 'Traditional', 'Normal', 'Youth', 'TA']  # 自定义标签

for i in range(5):
    plt.scatter(
        X.values[y_kmeans == i, 0],   # 年收入
        X.values[y_kmeans == i, 1],   # 消费指数
        s=100, c=colors[i], label=labels[i]
    )

# 绘制聚类中心
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=300, c='black', marker='X', label='Centroids'
)

plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()