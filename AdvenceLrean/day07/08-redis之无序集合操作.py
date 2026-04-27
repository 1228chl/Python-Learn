"""
存储形式: 无序不重复的数据集合  key->value(集合类型 多个值 {值1, 值2, ...})
列表应用场景: 数据去重  共同好友  添加标签
"""
import redis

# 1-创建连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password=None, decode_responses=True)

# 添加元素
r.sadd('tags', 'tag1', 'tag2', 'tag3')

# 获取所有元素
print(r.smembers(name='tags'))

# 判断元素是否存在
# 1:存在 0:不存在
print(r.sismember(name='tags', value='tag1'))

# 获取集合元素数量
print(r.scard(name='tags'))

# 随机弹出(删除)一个元素
# r.spop(name='tags')
# print(r.smembers(name='tags'))

# 移除指定元素
r.srem('tags', 'tag1')
print(r.smembers(name='tags'))

# 集合运算
r.sadd('set1', 'a', 'b', 'c')
r.sadd('set2', 'b', 'c', 'd')

# 交集
print(r.sinter('set1', 'set2'))
print(r.sinter(['set1', 'set2']))

# 并集
print(r.sunion('set1', 'set2'))
print(r.sunion(['set1', 'set2']))

# 差集
# set1 - set2
print(r.sdiff('set1', 'set2'))
# set2 - set1
print(r.sdiff(['set2', 'set1']))
