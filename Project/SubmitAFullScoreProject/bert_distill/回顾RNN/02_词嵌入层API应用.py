# 导包
import jieba
import torch.nn

# TODO 1.提前准备句子
text = '北京冬奥的进度条已经过半,不少外国运动员在完成自己的比赛后踏上归途!'
print(text)
# TODO 2.分词
# cut_all=False:代表精确模式
all_words = jieba.lcut(text, cut_all=False)
print(all_words)
# TODO 3.构建词表
# 3.1 先去重
unique_words = list(set(all_words))
# 3.2 构建词表
words2index = {words: index for index, words in enumerate(unique_words)}
print(words2index)
index2words = {index: words for index, words in enumerate(unique_words)}
print(index2words)
# TODO 4.构建词嵌入层
# num_embeddings给的是18: 告诉底层生成18个词向量,对应索引0-17
embed = torch.nn.Embedding(num_embeddings=len(unique_words), embedding_dim=4)
# TODO 5.生成词向量
for word, index in words2index.items():
    embeding = embed(torch.tensor(index))
    print(f"词:{word}->索引:{index}->向量:{embeding}")
