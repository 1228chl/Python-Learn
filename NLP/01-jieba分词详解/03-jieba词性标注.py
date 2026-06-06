# 导包
import jieba.posseg as pseg
# 准备句子
text = '我爱中国深圳,来了深圳就是深圳人'
# pseg->先分词再词性标注
my_list = pseg.lcut(text)
# 提取所有的,人名地名
for word ,pos in my_list:
    if pos == 'nr':
        print(word)
    if pos == 'ns':
        print(word)

