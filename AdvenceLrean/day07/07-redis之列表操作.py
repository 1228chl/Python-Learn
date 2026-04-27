"""
存储形式: 有序可重复的数据序列  key->value(列表形式, 多个值 [值1, 值2, ...])
列表应用场景: 消息队列中
"""
import redis

# 1-创建连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password=None, decode_responses=True)

r.flushdb()
# 从左添加数据
r.lpush('task:001', 'task1', 'task2', 'task3')
# 从右添加数据
r.rpush('task:001', 'task4', 'task5')

# 查看列表长度
print(r.llen(name='task:001'))

# 获取列表所有数据
# 左闭右闭
print(r.lrange(name='task:001', start=0, end=-1))

# 获取列表指定数据
print(r.lrange(name='task:001', start=0, end=2))
print(r.lrange(name='task:001', start=-2, end=-1))

# 从左弹出列表数据
r.lpop(name='task:001', count=2)
r.lpop(name='task:001')
print(r.lrange(name='task:001', start=0, end=-1))

# 从右弹出列表数据
r.rpop(name='task:001')
print(r.lrange(name='task:001', start=0, end=-1))