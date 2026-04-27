"""
存储形式: key -> value(多组值 name:张三 age:18 city:深圳)
哈希应用场景: 存储对象  用户信息  订单信息  一整串信息
"""
import redis
import warnings
warnings.filterwarnings(action='ignore')

# 1-创建连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password=None, decode_responses=True)

# 2-设置单个键值对
r.hset(name='user:001', key='name', value='张三')
r.hset(name='user:001', key='age', value='18')
r.hset(name='user:001', key='city', value='深圳')
# 3-获取单个值
print(r.hget(name='user:001', key='name'))
print(r.hget(name='user:001', key='age'))
print(r.hget(name='user:001', key='city'))

# 4-获取所有值
result1 = r.hgetall(name='user:001')
print('result1--->', type(result1), result1)

# 5-设置多个键值对
r.hmset(name='user:002', mapping={'name': '李四', 'age': 22})
result2 = r.hgetall(name='user:002')
print('result2--->', type(result2), result2)

# 6-获取多个值
print(r.hmget(name='user:001', keys=['name', 'age']))

# 7-获取所有键
print(r.hkeys(name='user:001'))

# 8-获取所有值
print(r.hvals(name='user:001'))

# 9-删除对应的值
r.hdel('user:001', 'name', 'age')
print(r.hgetall('user:001'))

r.flushdb()