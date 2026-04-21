import math,re
# 1. 生成批次歌词数据.
def data_loader(batch_size):
    with open('data/jaychou_lyrics.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    total = len(lines)
    total_batch = math.ceil(total / batch_size)
    for i in range(total_batch):
        print('当前批次：',i)
        yield lines[i*batch_size:(i+1)*batch_size]
if __name__ == '__main__':
    res = data_loader(10)
    for item in res:
        print(item)

# 2. 正则的几个案例.
# 	①需求：在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear
fruit = ['apple','banana','mango','orange','pear']
for item in fruit:
    res1 = re.match('apple|pear', item)
    print(res1)


# 	②需求：匹配出163、126、qq等邮箱
res2 = re.match('^[0-9a-zA-Z]{6,12}@(163|126|qq)\\.(com|edu)$','2124159894@qq.com')
print(res2)


# 	③需求 :  匹配qq:10567这样的数据，提取出来qq文字和qq号码
res3 = re.match('^(qq):(\\d{6,10})$','qq:1235553')
print(res3.group(1))
print(res3.group(2))


# 	④需求：匹配出<html>hh</html>
res4 = re.match(r'<([a-zA-Z][a-zA-Z0-9]*)>.*</\1>','<a>hh</a>')
print(res4)


# 	⑤需求：匹配出<html><h1>www.itcast.cn</h1></html>
res5 = re.match(r'<([a-zA-Z][a-zA-Z0-9]*)><([a-zA-Z][a-zA-Z0-9]*)>.*</\2></\1>','<html><h1>www.itcast.cn</h1></html>')
print(res5)






