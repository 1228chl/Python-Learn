import redis

# 1-创建连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password=None, decode_responses=True)

# 设置键值对
r.set(name='session:user001', value='user_data')

# 检查键是否存在
# 返回0 或 1
print(r.exists('session:user001'))
print(r.exists('set1'))

# 设置过期时间（秒）
r.expire(name='session:user001', time=30)
r.expire(name='set1', time=300)

# 获取剩余生存时间
print(r.ttl(name='set1'))

# 设置键值对并指定过期时间
r.setex(name='session:user002', value='user_data', time=30)

# 移除过期时间，使键永久存在
r.persist(name='session:user002')

# 查找匹配模式的键
print(r.keys(pattern='*'))
print(r.keys(pattern='session:*'))

# 删除键
r.delete('session:user002', 'set1', 'set2')