# 导包
import jieba
import torch.nn

# 提前准备句子
text = '北京东奥的进度条已经过半，不少外国运动员在完成自己的比赛后踏上归途！'
# cut_all=False:代表精确模式
all_words = jieba.lcut(text,cut_all=False)
print(all_words)
# 构建词表
# 3.1 先去重
unique_words = list(set(all_words))
# 3.2 构建词表
word2index = {word:index for index, word in enumerate(unique_words)}
print(word2index)
index2words = {index:word for index, word in enumerate(unique_words)}
print(index2words)
# 4.构建词嵌入层
embed = torch.nn.Embedding(len(unique_words),embedding_dim=4)
# 5.生成词向量
for word,index in word2index.items():
    embedding = embed(torch.tensor([index]))
    print(f"词：{word}->索引：{index}->向量：{embedding}")