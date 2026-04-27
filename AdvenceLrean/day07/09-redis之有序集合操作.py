"""
存储形式: 有序的数据集合  key->value(字典形式 多个值 {value1:分值1, value2:分值2, ...})
列表应用场景:
"""
import redis

# 1-创建连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password=None, decode_responses=True)

# 添加带分数的元素
r.zadd('leaderboard', {
    'player1': 1000,
    'player2': 1500,
    'player3': 800,
    'player4': 2000
})

# 按分数升序获取
# start end: 获取的范围
# withscores: 是否返回分数
print(r.zrange(name='leaderboard', start=0, end=-1, withscores=True))

# 按分数降序获取
print(r.zrevrange(name='leaderboard', start=0, end=-1, withscores=True))

# 获取元素分数
print(r.zscore(name='leaderboard', value='player1'))

# 增加元素分数
r.zincrby(name='leaderboard', amount=200, value='player1')
print(r.zscore(name='leaderboard', value='player1'))
# 减少元素分数  负分
r.zincrby(name='leaderboard', amount=-100, value='player1')
print(r.zscore(name='leaderboard', value='player1'))

# 获取排名
# 升序排名, 默认从0开始
print(r.zrank(name='leaderboard', value='player1'))
# 降序排名, 默认从0开始
print(r.zrevrank(name='leaderboard', value='player1'))

# 按分数范围获取
print(r.zrange(name='leaderboard', start=0, end=-1, withscores=True))
# min max:左闭右闭
print(r.zrangebyscore(name='leaderboard', min=1100, max=2000))