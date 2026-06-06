# 导包
import jieba
from tensorflow.keras.preprocessing.text import Tokenizer
import joblib

# 模拟准备数据
words = ['张三', '李四', '王五', '赵六', '田七']
def base_one_hot():
    # 构建词表
    index2word = {index:word for index,word in enumerate(words)}
    word2index = {word:index for index,word in enumerate(words)}
    # 构建one-hot向量
    for word in words:
        # 1.先制作全0且维度是词个数的列表
        zero_list = [0] * len(words)
        print(zero_list)
        # 2.每个词对应位置设置为1
        index = word2index[word]
        zero_list[index] = 1
        print(zero_list)

def tonkenizer_one_hot():
    # 1.实例化Tokenizer并拟合
    tokenzier = Tokenizer()
    tokenzier.fit_on_texts(words)
    print(tokenzier.word_index)
    print(tokenzier.index_word)
    # 构建one-hot向量
    for word in words:
        # 1.先制作全0且维度是词个数的列表
        zero_list = [0] * len(words)
        # 2.每个词对应位置设置为1
        index = tokenzier.word_index[word]
        zero_list[index] = 1
        print(zero_list)
    # 保存tokenizer
    joblib.dump(tokenzier,'/my_tokenizer')

if __name__ == '__main__':
    # 手动方式
    base_one_hot()
    # Tokenzier方式
    # 提前安装:tensorflow
    tonkenizer_one_hot()
    tokenzier = joblib.load('/my_tokenizer')
    print(tokenzier.word_index)
