"""
match(正则表达式, 字符串, 修饰符): 从字符串的第一个字符根据正则表达式开始进行匹配
匹配成功返回对象, 对象.group() 获取匹配成功的数据
匹配失败返回None, None没有group(), None.group()会发生报错
注意点: 从字符串的开头匹配

search(正则表达式, 字符串, 修饰符): 扫描整个字符串, 返回第一个匹配成功的子串
匹配成功返回对象, 对象.group() 获取匹配成功的数据
匹配失败返回None, None没有group(), None.group()会发生报错
注意点: 不是从字符串的开头匹配
"""

import re

# todo:1-match
# pattern: 参数值就是正则表达式
# .: 匹配除\n外的任意单个字符
# result = re.match(pattern='.it.', string='ait1')
result = re.match(pattern='.it.', string='\nit1')  # 匹配失败
if result:
    print('匹配成功...')
    print('匹配到的子串数据是:', result.group())
else:
    print('匹配失败...')

print('=' * 80)

# todo:2- search
# 从字符串的任意位置开始匹配, 返回第一个匹配成功的子串
# result = re.search(pattern='it.', string='itcastitcastitcast')
result = re.search(pattern='it.', string='castitcastitcast')
if result:
    print('匹配成功...')
    print('result--->', result)
    print('匹配到的子串数据是:', result.group())
else:
    print('匹配失败...')

