import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# 读取数据（请根据实际文件路径调整）
taitan_df = pd.read_csv("./data/train.csv")

# 查看前5行
print("前5行数据:")
print(taitan_df.head())

# 查看数据信息（包括缺失值、数据类型）
print("\n数据信息:")
print(taitan_df.info())

# 查看目标值分布
print("\n生存情况统计:")
print(taitan_df['Survived'].value_counts())
print(f"生存率: {taitan_df['Survived'].mean():.2%}")

# 确定特征 X 和目标 y
X = taitan_df[['Pclass', 'Age', 'Sex']]
y = taitan_df['Survived']

print("原始特征数据前5行:")
print(X.head())

# 检查缺失值
print("缺失值统计:")
print(X.isnull().sum())

# 使用年龄的平均值填充缺失值
X['Age'].fillna(X['Age'].mean(), inplace=True)

# 验证缺失值已处理
print("\n填充后缺失值统计:")
print(X.isnull().sum())

# 查看编码前的数据
print("编码前的特征:")
print(X.head())

# 进行 one-hot 编码（drop_first=False 保留所有分类）
X = pd.get_dummies(X, columns=['Sex'], drop_first=False)

print("\n编码后的特征:")
print(X.head())
print("\n特征列名:", X.columns.tolist())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=33
)

print(f"训练集样本数: {X_train.shape[0]}")
print(f"测试集样本数: {X_test.shape[0]}")

# 实例化决策树分类器（使用默认参数，也可设置 max_depth 限制）
estimator = DecisionTreeClassifier(random_state=42)

# 训练模型
estimator.fit(X_train, y_train)

# 在测试集上预测
y_pred = estimator.predict(X_test)

# 计算准确率
accuracy = estimator.score(X_test, y_test)
print(f"测试集准确率: {accuracy:.4f}")

# 使用 classification_report
report = classification_report(y_test, y_pred, target_names=['遇难', '幸存'])
print("\n分类报告:")
print(report)

plt.figure(figsize=(30, 20))  # 设置画布大小
plot_tree(
    estimator,
    max_depth=4,                # 只显示前4层，避免过于拥挤
    filled=True,               # 节点填充颜色（类别不同颜色不同）
    feature_names=['Pclass', 'Age', 'Sex_female', 'Sex_male'],
    class_names=['遇难', '幸存'],
    rounded=True,
    fontsize=12
)
plt.title("泰坦尼克号生存预测决策树")
plt.show()