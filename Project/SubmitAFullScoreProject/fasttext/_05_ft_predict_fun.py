# 导包
import fasttext
import jieba

from _01_config import Config

# TODO 提前创建配置对象
config = Config()

# TODO 加载模型
model = fasttext.load_model(config.ft_word_auto_model_path)


# TODO 定义API接口函数
def predict_fun(data):
    # todo 1. json数据中获取文本,然后直接做分词
    words = " ".join(jieba.lcut(data['test']))
    # todo 2. fasttext模型直接预测
    y_pred_tuple = model.predict([words])
    print(y_pred_tuple)  # (('__label__education',), array([1.00000978]))
    # todo 3. 从结果中获取类别名
    y_pred_class = y_pred_tuple[0][0][0][9:]
    # todo 4. 拼接到data中返回
    data['predict_class'] = y_pred_class
    # 返回
    return data

if __name__ == '__main__':
    # 模拟准备json格式数据
    # test = '词汇阅读是关键 08年考研暑期英语复习全指南'
    text = input('请您输入一个新闻:')
    data = {"test": text}
    # TODO 模拟调用API
    result = predict_fun(data)
    print(result)
