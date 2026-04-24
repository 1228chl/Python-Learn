"""
修饰符: 给正则表达式添加其他的限定

使用:
可选项  re.match(flags=修饰符)
多个修饰符   修饰符1 | 修饰符2

常用修饰符:
re.I -> 忽略大小写
re.S -> .可以匹配\n
"""
import re

my_str = 'Hi!\n456\n789'

# re.I
# result = re.match(pattern='^[a-z]i!', string=my_str)  # 匹配失败 H是大小, 我们规则是小写
result = re.match(pattern='^[a-z]i!', string=my_str, flags=re.I)
print('result--->', result.group())

print('=' * 80)


# re.S
# result = re.match(pattern='.{6}', string=my_str)  # 匹配失败 .不能匹配\n
result = re.match(pattern='.{6}', string=my_str, flags=re.S)
print('result--->\n', result.group())

print('=' * 80)

# 多个修饰符
result = re.match(pattern='[a-z].{6}', string=my_str, flags=re.I | re.S)
print('result--->', result.group())