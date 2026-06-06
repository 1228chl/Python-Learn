# 导包
import fasttext

def train_model():
    # fasttext 训练词向量
    path = r"data/fil9"
    # 注意:当前为了快速看结果,轮次比较少
    model = fasttext.train_unsupervised(path,model='skipgram',ws=5,dim=3,epoch=5)
    # 保存模型
    model.save_model('data/skipgram.bin')

def test_model():
    # 加载模型
    model = fasttext.load_model(r'data/skipgram.bin')
    # 获取某个单词词向量
    data = model.get_word_vector('working')
    print(data)
    # 获取某个单词的相似的k个
    data = model.get_nearest_neighbors('working',k=5)
    print(data)
    # 获取子词
    data =model.get_subwords('apple')
    print(data)

if __name__ == '__main__':
    train_model()
    test_model()