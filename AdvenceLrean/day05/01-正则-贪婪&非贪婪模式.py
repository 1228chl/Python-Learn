"""
贪婪: 正则表达式默认是贪婪模式, 在匹配成功前提下, 尽可能匹配更多的子串  .*  .+
非贪婪: 在匹配成功前提下, 尽可能匹配更少的子串  ?来限制   .*?  .+?
"""
import re

str1 = '<h1>编程语言</h1>又开始谈判, 谈不成接着打<h1>Python+AI</h1>'
# 贪婪模式
# .* -> 编程语言</h1>又开始谈判, 谈不成接着打<h1>Python+AI
result = re.findall(pattern=r'<h1>.*</h1>', string=str1)
print('result--->', result)

print('=' * 80)

# 非贪婪模式
# .*? -> 第1部分: 编程语言  第2部分: Python+AI
result = re.findall(pattern=r'<h1>.*?</h1>', string=str1)
print('result--->', result)

print('=' * 80)

# 非贪婪模式 + 分组
result = re.findall(pattern=r'<h1>(.*?)</h1>', string=str1)
print('result--->', result)

print('=' * 80)

# 两个分组
result = re.match(pattern=r'<h1>(.*?)</h1>.*<h1>(.*?)</h1>', string=str1)
if result:
    g1 = result.group(1)  # 分组1: 编程语言
    print('g1--->', g1)
    g2 = result.group(2)  # 分组2: Python+AI
    print('g2--->', g2)
else:
    print('没有匹配到内容...')
