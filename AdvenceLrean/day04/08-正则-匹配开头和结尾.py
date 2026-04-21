import re

# todo:1- ^: 匹配字符串开头
# 匹配第一个字符为数字
# result = re.match(pattern='^\d', string='22itcast')
# 匹配第一个字符为数字, 匹配多个数字
# result = re.match(pattern='^\d+', string='22itcast')
# result = re.match(pattern='^\d+itcast', string='22itcast')
# result = re.match(pattern='^\d.*', string='22itcast')
# result = re.match(pattern='^\ditcast', string='22itcast')  # 失败
# 匹配第一个字符为数字, 最少1次最多3次
# result = re.match(pattern='^\d{1,3}.*', string='22itcast')
# result = re.match(pattern='^\d{1,3}.*', string='22367itcast')

# result = re.search(pattern='itcast', string='22itcast33itcast')
# result = re.search(pattern='^itcast', string='22itcast33itcast')  # 失败, 开头的字符不是i

# todo:2- $: 匹配字符串结尾
# 匹配手机号: 限制11位数字
# result = re.match(pattern='\d{11}', string='12345678901')
# result = re.match(pattern='\d{11}$', string='1234567890174657')  # 失败
# result = re.match(pattern='\d{11}$', string='1234567890')  # 失败
# 以数字开头 以数字结尾
# result = re.match('^\d.*\d$', string='22itcast33')
# result = re.match('^\d+.*\d$', string='22itcast33')
# result = re.match('^\d+.*\d+$', string='22itcast33')
# result = re.match('^\d+.*\d+$', string='22itcast33a')  # 失败
result = re.match('^\\d+.*\\d+$', string='a22itcast33')  # 失败
if result:

    print('匹配到的子串数据是:', result.group())
else:
    print(f'匹配失败: {result}')
