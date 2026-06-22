# 导包
import jieba

# TODO 提前准备句子
text = '北京冬奥的进度条已经过半,不少外国运动员在完成自己的比赛后踏上归途!'
print(text)
print('==================================================')
# TODO 中文分词方式1: 直接列表转换 一个个字符分开
words = list(text)
print(words)
print('==================================================')
# TODO 中文分词方式2: jieba分词 自然习惯去分且有3种方式
# cut_all=False:代表精确模式
c1 = jieba.lcut(text, cut_all=False)
print(c1)
# cut_all=True:代表全模式
c2 = jieba.lcut(text, cut_all=True)
print(c2)
# 搜索引擎模式
c3 = jieba.lcut_for_search(text)
print(c3)
