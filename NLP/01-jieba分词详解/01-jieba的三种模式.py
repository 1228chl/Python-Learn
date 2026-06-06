#导包
import jieba

# 1.准备句子
text = '传智教育是一家上市公司，旗下有黑马程序员品牌，我正在黑马这里学AI！'
# 2.分词
# 注意cut()和lcut()区别:cut()返回生成器,lcut()返回列表(推荐)
# 2.1 精确模式
r1 = jieba.lcut(text,cut_all=False)
print(r1)

# 2.2 全模式
r2 = jieba.lcut(text,cut_all= True)
print(r2)
# 2.3 搜索引擎模式
r3 = jieba.lcut_for_search(text)
print(r3)
