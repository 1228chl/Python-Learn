import jieba
from _01_config import Config
import pickle

config = Config()

# 2.加载tfidf
with open(config.tfidf_save_path,'rb') as f:
    tfidf = pickle.load(f)

# 3.加载rf模型
with open(config.rf_save_model_path,'rb') as f:
    model = pickle.load(f)

# 4.定义api接口
def predict_fun(data):
    # 4.1 json数据中获取文本，然后直接做分词
    words = " ".join(jieba.lcut(data['text']))

    # 4.2 tfidf文本转数据特征
    number_words = tfidf.transform([words])

    # 4.3 rf莫i选哪个预测类别索引
    y_pred_list = model.predict(number_words)
    y_pred_idx = y_pred_list[0]

    # 4.4 根据索引获取中文类别
    id2class = {index: line.strip() for index,line in enumerate(open(config.class_path,'r',encoding='utf-8'))}
    y_pred_class = id2class[y_pred_idx]

    # 4.5 拼接到data中并返回
    data['predict_class'] = y_pred_class

    # 返回
    return data

if __name__ == '__main__':
    #  模拟页面传递过来json数据
    text = input('请输入一个新闻')
    data = {"text": text}

    # 模拟调用api
    result = predict_fun(data)
    print(result)
