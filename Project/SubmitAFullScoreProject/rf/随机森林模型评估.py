import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from config import Config
import pickle

# 1.提前创建配置对象
config = Config()
# 2.读取测试集分词后数据，同时获取特征和标签
df_data = pd.read_csv(config.process_test_path,sep='\t')
x_words = df_data['words']
y_label = df_data['label']
# 3.加载tfidf然后把文本数据转换为数值数据
with open(config.tfidf_save_path,'rb') as f:
    tfidf = pickle.load(f)
new_x_words = tfidf.transform(x_words)
# 4.加载rf模型然后预测
with open(config.rf_save_model_path,'rb') as f:
    model = pickle.load(f)
y_pred = model.predict(new_x_words)
# 5.评估
print(f'准确率：{accuracy_score(y_label,y_pred)*100:.2f}%')
print(f'精确率：{precision_score(y_label,y_pred,average='macro')*100:.2f}%')
print(f'召回率：{recall_score(y_label,y_pred,average='macro')*100:.2f}%')
print(f'F1-score：{f1_score(y_label,y_pred,average='macro')*100:.2f}%')
