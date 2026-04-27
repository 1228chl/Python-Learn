"""
存储形式: key -> value(一个值 张三)
字符串应用场景: 缓存 计数器
"""
import redis

# 1-创建连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password=None, decode_responses=True)

# 2-设置键值对
r.set(name='name', value='张三')
r.set('age', '18')
# 设置多个键值对
r.mset(mapping={'job': 'AI大模型开发', 'city': '深圳', 'salary': 20000})

# 3-获取键对应的值
name = r.get('name')
age = r.get('age')
print(f'name的值是:{name}, age的值是:{age}')
# 获取多个值
values = r.mget(['name', 'age', 'job', 'city', 'salary'])
print(f'values的值是:{values}')

# 4-设置键值对并设置过期时间
# name: 键
# value: 值
# time: 过期时间
r.setex(name='sex', value='男', time=10)

print('==================================计算器==================================')
# 设置初始计算器 0
r.set(name='count', value=0)
print(r.get('count'))
# 增加 +1
r.incr(name='count', amount=1)
print(r.get('count'))
# 增加指定的数值
r.incrby(name='count', amount=5)
print(r.get('count'))

# 减少 -1
r.decr(name='count', amount=1)
print(r.get('count'))
# 减少指定的数值
r.decrby(name='count', amount=5)
print(r.get('count'))

# r.flushdb()  # 清空当前数据库
# r.flushall() # 清空所有数据库

