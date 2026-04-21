import re

# todo:1- 表达式1|表达式2: 匹配左右任意一个表达式
# 需求: 获取 水果列表中 为 apple和pear的两种水果
fruits = ['apple', 'pear', 'orange', 'banana', 'grape']
# 循环遍历水果列表, 一个一个进行匹配处理
for fruit in fruits:
    result = re.match(pattern='apple|pear', string=fruit)
    if result:
        print(f'我想吃的水果是: {result.group()}')
    else:
        print(f'不想吃的水果是:{fruit}')

print('=' * 80)

# todo:2- (): 分组
"""
需求: 匹配 163 126 qq 邮箱   871234678@163.com
@前可以是4-20位数字字母下划线
以.com结尾
"""
# 表达式1: [0-9a-zA-Z_]{4,20}@163  表达式2: 126 表达式3: qq.com  -> 成功匹配到 871234678@163 第一个表达式
# result = re.match(pattern='[0-9a-zA-Z_]{4,20}@163|126|qq.com', string='871234678@163.com')
# (163|126|qq): 分组, 匹配分组内的任意一个表达式
# result = re.match(pattern='[0-9a-zA-Z_]{4,20}@(163|126|qq).com', string='871234678@163.com')
# .: 匹配除\n外的任意单个字符
# result = re.match(pattern='[0-9a-zA-Z_]{4,20}@(163|126|qq).com', string='871234678@163ccom')
# result = re.match(pattern='[0-9a-zA-Z_]{4,20}@(163|126|qq)\.com', string='871234678@163.com')
# $: 匹配字符串结尾
# result = re.match(pattern='[0-9a-zA-Z_]{4,20}@(163|126|qq)\.com', string='871234678@163.comnhkdshagkdfsa')
result = re.match(pattern='[0-9a-zA-Z_]{4,20}@(163|126|qq)\\.com$', string='871234678@163.com')
if result:
    print(f'匹配到的子串是: {result.group()}')
else:
    print(f'匹配失败: {result}')

print('=' * 80)
# todo:3- (): 分组, 获取分组的数据 group(1) group(2) -> 提取想要的数据(想要什么数据就进行分组即可)
"""
需求: qq号格式 -> qq: 871234678  提取 qq 和 871234678 这两部分内容
qq号是4-11位数字
"""
# result = re.match(pattern='qq: \d{4,11}$', string='qq: 871234678')
result = re.match(pattern='(qq): (\\d{4,11})$', string='qq: 871234678')
if result:
    print(f'匹配到的子串是: {result.group()}')
    print(f'匹配到的子串是: {result.group(0)}')
    type1 = result.group(1)
    num = result.group(2)
    print(f'类型是: {type1}, qq号是: {num}')
else:
    print(f'匹配失败: {result}')


# todo:4- (): 分组, 不起别名可以通过\1,\2引用分组  起别名 (?P<name>), 使用分组别名 (?P=name)
# 一般可以在html数据中使用
# <h1></h1>  <html></html>
# <h1><html>哈哈哈</html></h1>
# result = re.match(pattern='<([a-zA-Z][a-zA-Z1-6]{1,3})>.*</([a-zA-Z][a-zA-Z1-6]{1,3})>', string='<h1>哈哈哈</h1>')
# result = re.match(pattern='<([a-zA-Z][a-zA-Z1-6]{1,3})>.*</([a-zA-Z][a-zA-Z1-6]{1,3})>', string='<html>哈哈哈</html>')
# 引用分组 第一组:\1 第二组:\2  一个\表示转译, \1->\不是转译的意思
# result = re.match(pattern='<([a-zA-Z][a-zA-Z1-6]{1,3})>.*</\\1>', string='<html>哈哈哈</html>')
# 分组起别名
result = re.match(pattern='<(?P<name1>[a-zA-Z][a-zA-Z1-6]{1,3})>.*</(?P=name1)>', string='<html>哈哈哈</html>')
if result:
    print(f'匹配到的子串是: {result.group()}')
else:
    print(f'匹配失败: {result}')
