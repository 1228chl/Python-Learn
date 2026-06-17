batch = [('词汇阅读是关键 08年考研暑期英语复习全指南', 3), ('中国人民公安大学2012年硕士研究生目录及书目', 3), ('日本地震：金吉列关注在日学子系列报道', 3), ('名师辅导：2012考研英语虚拟语气三种用法', 3)]
# 方法1: 推导式
texts = [t[0] for t in batch]
labels = [t[1] for t in batch]
print(texts)
print(labels)
# 方法2: zip
texts2,labels2 = zip(*batch)
print(texts2)
print(labels2)
