# 导包
import torch
# 准备数据
words = ['我','爱','你']

# 创建词嵌入层
embed = torch.nn.Embedding(num_embeddings=len(words), embedding_dim=4)
# 获取词向量
for word,index in enumerate(words):
    print(f'词:{word}->索引:{index}->向量:{embed(torch.tensor(index))}')