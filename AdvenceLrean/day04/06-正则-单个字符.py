import re

# todo:1- .: 匹配除\n外的任意单个字符
# result = re.match(pattern='.t', string='itcast')
# result = re.match(pattern='.t', string='\ntcast')
# result = re.match(pattern='.t', string='\ttcast')
# result = re.match(pattern='.t', string='$tcast')
# result = re.match(pattern='..', string='$tcast')  # .. -> 两个字符
# \. -> 匹配 ., 不再表示除\n外的任意单个字符
# result = re.match(pattern='\.t', string='.tcast')


# todo:2- []: 匹配列表中列举的任意单个字符
# result = re.match(pattern='[1234]', string='123abc')
# result = re.match(pattern='[1234]2', string='123abc')
# 0-9:表示 0,1,2...,9 10个数字
# a-z:表示 a,b,c...,z 26个字母
# result = re.match(pattern='[0-9a-zA-Z_]2', string='123abc')
# [^]:取反, 匹配非列表中列举的任意单个字符
# result = re.match(pattern='[^0-9a-zA-Z_]2', string='123abc')
# result = re.match(pattern='[^0-9a-zA-Z_]2', string='@23abc')

# todo:3- \d: 匹配数字 0-9  \D: 匹配非数字
# result = re.match(pattern='\d', string='123abc')
# result = re.match(pattern='\d\d', string='123abc')
# result = re.match(pattern='\D', string='i23abc')

# todo:4- \s: 匹配空白字符 空格 tab键 \n  \S: 匹配非空白字符
# result = re.match(pattern='\s', string=' 12345')
# result = re.match(pattern='\s', string='    12345')
# result = re.match(pattern='\s', string='\t12345')
# result = re.match(pattern='\S', string='\t12345')  # 失败
# result = re.match(pattern='\S', string='\n12345')  # 失败
# result = re.match(pattern='\S', string='@12345')  # 失败

# todo:5- \w: 匹配非特殊字符 数字 字母 下划线 汉字  \W: 匹配特殊字符
# result = re.match(pattern='\w23abc', string='123abc')
# result = re.match(pattern='\w23abc', string='好23abc')
# result = re.match(pattern='\w23abc', string='_23abc')
# result = re.match(pattern='\w23abc', string='A23abc')
# result = re.match(pattern='\w23abc', string='a23abc')
# result = re.match(pattern='\W23abc', string='a23abc')
# result = re.match(pattern='\W23abc', string='\t23abc')
result = re.match(pattern='\W23abc', string='\n23abc')
if result:
    print(f'匹配成功, 匹配到的子串是:{result.group()}')
else:
    print(f'匹配失败, 内容为:{result}')
