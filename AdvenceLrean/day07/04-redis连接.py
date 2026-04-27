import redis

# 查看redis数据库的版本
print(redis.__version__)

# 创建连接对象
# decode_responses: 是否返回字符串类型的数据
r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                password=None,
                decode_responses=True)
print(r)
# 返回True表示连接成功
print(r.ping())
