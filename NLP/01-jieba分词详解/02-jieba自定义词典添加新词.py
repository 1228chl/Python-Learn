# 安装: pip install jieba
# 导包
import jieba

#  1.准备句子
text = '传智教育是一家上市公司,旗下有黑马程序员品牌,我正在黑马这里学习AI!'
# TODO 方式1: 加载用户自定义词典
# jieba.load_userdict('words.txt')
# TODO 方式2: 直接加词到默认词典中
jieba.add_word('传智教育')
jieba.add_word('黑马程序员',freq=1000, tag='n')
jieba.add_word('下有',freq=0)
# 2.分词
# 注意: cut()和lcut()区别: cut()返回生成器,lcut()返回列表(推荐)
# 2.1 精确模式
r1 = jieba.lcut(text, cut_all=False)
print(r1)
# 2.2 全模式
r2 = jieba.lcut(text, cut_all=True)
print(r2)
# 2.3 搜索引擎模式
r3 = jieba.lcut_for_search(text)
print(r3)
