from config.config import Config
import pandas as pd
import sklearn
import pickle
import time
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# 1.提前创建Config对象
config = Config()

# 2.读取分词后的数据文件
train_df = pd.read_csv(config.process_train_path, sep='\t')
dev_df = pd.read_csv(config.process_dev_path, sep='\t')
test_df = pd.read_csv(config.process_test_path, sep='\t')

print(f"训练集: {len(train_df)}, 验证集: {len(dev_df)}, 测试集: {len(test_df)}")


# 3.使用TFIDF把文本特征转换为数值特征
# 3.1 提前将停用词获取
stop_words = [line.strip() for line in open(config.stop_words, 'r', encoding='utf-8')]

# 3.2 创建TFIDF对象并设置停用词
tfidf = sklearn.feature_extraction.text.TfidfVectorizer(
    stop_words=stop_words,
    max_features=50000,          # 只保留最重要的 5 万个词
    min_df=5,                    # 忽略出现次数少于 5 的词汇
    max_df=0.7,                  # 忽略出现在 70% 以上文档的词汇（高频停用词）
    ngram_range=(1, 2),      # 保留二元词组
    sublinear_tf=True            # 使用 1+log(tf) 平滑
)

#  4 训练文本特征转数值特征
print("开始 TF-IDF 转换...")
start_time = time.time()
X_train = tfidf.fit_transform(train_df['words'])
X_dev = tfidf.transform(dev_df['words'])
X_test = tfidf.transform(test_df['words'])
print(f"TF-IDF 转换完成，训练集特征维度: {X_train.shape}，耗时 {time.time()-start_time:.2f} 秒")

y_train = train_df['label']
y_dev = dev_df['label']
y_test = test_df['label']

# 5.随机森林模型训练
# 5.1 创建随机森林模型对象
model = sklearn.ensemble.RandomForestClassifier(
    n_estimators=200,            # 树的数量，可根据时间调整（50~200）
    max_depth=20,                # 限制深度减少过拟合，也加速
    min_samples_split=10,        # 内部节点再划分所需最小样本数
    min_samples_leaf=3,
    max_features='sqrt',
    n_jobs=-1,                   # 使用所有 CPU 核心
    random_state=42,
    class_weight='balanced_subsample',
    verbose=2
)

# 5.2 模型训练
print("开始训练随机森林...")
start_time = time.time()
model.fit(X_train, y_train)
print(f"训练结束，耗时 {(time.time() - start_time):.2f} 秒")


# 6. 在验证集上评估（用于调参）
y_pred_dev = model.predict(X_dev)
print("\n【验证集结果】")
print(f"准确率: {accuracy_score(y_dev, y_pred_dev)*100:.2f}%")
print(f"精确率 (macro): {precision_score(y_dev, y_pred_dev, average='macro')*100:.2f}%")
print(f"召回率 (macro): {recall_score(y_dev, y_pred_dev, average='macro')*100:.2f}%")
print(f"F1-score (macro): {f1_score(y_dev, y_pred_dev, average='macro')*100:.2f}%")
from sklearn.metrics import classification_report
print(classification_report(y_dev, y_pred_dev, digits=4))

# 7. 最终在测试集上评估（仅一次）
y_pred_test = model.predict(X_test)
print("\n【测试集最终结果】")
print(f"准确率: {accuracy_score(y_test, y_pred_test)*100:.2f}%")
print(f"精确率 (macro): {precision_score(y_test, y_pred_test, average='macro')*100:.2f}%")
print(f"召回率 (macro): {recall_score(y_test, y_pred_test, average='macro')*100:.2f}%")
print(f"F1-score (macro): {f1_score(y_test, y_pred_test, average='macro')*100:.2f}%")

# 8.保存模型
with open(config.tfidf_save_path,'wb')as f:
    pickle.dump(tfidf,f)
with open(config.random_forests_save_model_path,'wb')as f:
    pickle.dump(model,f)
print("模型和向量器已保存。")