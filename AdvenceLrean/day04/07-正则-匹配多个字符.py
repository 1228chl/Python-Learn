import re

# todo:1- *: 匹配前一个字符出现0次或无数次
# result = re.match(pattern='6*', string='66666itcast')
# result = re.match(pattern='\d*', string='61686itcast')
# result = re.match(pattern='\d*', string='61a86itcast')
# result = re.match(pattern='[0-9]*', string='61a86itcast')
# result = re.match(pattern='.*', string='61a86itcast')
# result = re.match(pattern='6*', string='itcast')

# todo:2- +: 匹配前一个字符出现1次或无数次  +1->至少一次
# result = re.match(pattern='6+', string='6itcast')
# result = re.match(pattern='6+', string='666itcast')
# result = re.match(pattern='6+', string='itcast')  # 失败
# result = re.match(pattern='.+', string='itcast')
# result = re.match(pattern='\w+', string='itcast')

# todo:3- ?: 匹配前一个字符出现0次或1次
# result = re.match(pattern='6?itcast', string='itcast')
# result = re.match(pattern='6?', string='itcast')
# result = re.match(pattern='6?', string='6itcast')
# result = re.match(pattern='6?', string='66itcast')
# result = re.match(pattern='.?', string='66itcast')
# result = re.match(pattern='.?itcast', string='66itcast')  # 失败


# todo:4- {m}: 匹配前一个字符出现m次
# result = re.match(pattern='6{3}', string='66itcast')  # 失败
# result = re.match(pattern='6{3}', string='666itcast')
# result = re.match(pattern='\d{3}', string='666itcast')
# 匹配手机号: 限制11位数字
# result = re.match(pattern='\d{11}', string='12345678901')
# result = re.match(pattern='\d{11}', string='123456789012')  # 只匹配前11位数字的子串

# todo:5- {m,n}: 匹配前一个字符出现m到n次, 至少m次, 至多n次  注意点:m和n之间的逗号不能有空格
# 匹配密码: 至少6位, 最多12位
# result = re.match(pattern='.{6,12}', string='123')  # 失败
# result = re.match(pattern='.{6,12}', string='123abc')  # 6位
# result = re.match(pattern='.{6,12}', string='123abc456')  # 9位
# result = re.match(pattern='.{6,12}', string='123abc456efg')  # 12位
result = re.match(pattern='.{6,12}', string='123abc456efghierhiw')  # 大于12位  # 只匹配前12位的子串
# result = re.match(pattern='.{6, 12}', string='123abc456efghierhiw')  # 失败, 逗号后面有空格
if result:
    print('匹配到的子串数据是:', result.group())
else:
    print(f'匹配失败: {result}')

# res = re.match('^[0-9]{17}[0-9xX]$','36232920001010199x')
res = re.match('^\\d{17}[0-9xX]$', '36232920001010199x')
if res:
    print('匹配到的子串数据是:', res.group())
else:
    print(f'匹配失败: {res}')
