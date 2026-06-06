# 导包
import jieba.posseg as pseg
# todo 准备句子
text = '我爱中国深圳,来了深圳就是深圳人'
# TODO pseg->先分词再词性标注
my_list = pseg.lcut(text)
print(my_list)