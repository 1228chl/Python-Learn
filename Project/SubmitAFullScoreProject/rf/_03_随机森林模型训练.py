import pandas as pd
import sklearn
import pickle
import time
from _01_config import Config
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# 1.提前创建Config对象
config = Config()

# 2.读取分词后的数据文件
df_data = pd.read_csv(config.process_train_path,sep='\t')
print(df_data)
# 3.单独获取特征和标签
x_words = df_data['words']
y_labels = df_data['label']
# 4.使用TFIDF把文本特征转换为数值特征
# 4.1 提前将停用词获取
stop_words = [line.strip() for line in open(config.stop_words_path,'r',encoding='utf-8')]
# 4.2 创建TFIDF对象并设置停用词
tfidf = sklearn.feature_extraction.text.TfidfVectorizer(stop_words=stop_words)
#  4.3 训练文本特征转数值特征
words_feature = tfidf.fit_transform(x_words)
# print(words_feature)
# 5.随机森林模型训练
# 5.1 先切割数据
x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(words_feature,y_labels,test_size=0.2,random_state=1)

# 5.2 创建随机森林模型对象
model = sklearn.ensemble.RandomForestClassifier(verbose=2,n_jobs=-1)
# 5.3 模型训练
start_time = time.time()
print('开始训练了')
model.fit(x_train,y_train)
print(f'训练结束，耗时{(time.time()-start_time):.2f}秒')
# 6.随机森林模型预测
y_pred = model.predict(x_test)
# 7.随机森林模型评估
print(f'准确率：{accuracy_score(y_test,y_pred)*100:.2f}%')
print(f'精确率：{precision_score(y_test,y_pred,average='macro')*100:.2f}%')
print(f'召回率：{recall_score(y_test,y_pred,average='macro')*100:.2f}%')
print(f'F1-score：{f1_score(y_test,y_pred,average='macro')*100:.2f}%')
# 8.保存模型
with open(config.tfidf_save_path,'wb') as f:
    pickle.dump(tfidf,f)
with open(config.rf_save_model_path,'wb') as f:
    pickle.dump(model,f)
print('模型保存完成')
