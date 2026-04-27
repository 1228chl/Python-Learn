# 导包
import redis
import json
import time


# todo:1-创建缓存类
class RedisCache(object):
    # todo:2-init构造方法, 创建redis连接对象
    def __init__(self, host='localhost', port=6379, db=0):
        # 定义redis连接对象属性
        self.redis_client = redis.Redis(host=host,
                                        port=port,
                                        db=db,
                                        decode_responses=True)

    # todo:3-定义设置缓存的方法
    def set_cache(self, key, value, expire_time=3600):
        """
        设置缓存
        :param key: 键
        :param value: 值
        :param expire_time: 过期时间, 默认1个小时
        :return: 返回True或Fasle
        """
        try:
            # 3.1 将value转换成json数据格式
            value_str = json.dumps(value)
            # 3.2 设置缓存
            self.redis_client.setex(key, expire_time, value_str)
            return True
        except Exception as e:
            print(f'设置缓存失败: {e}')
            return False

    # todo:4-定义获取缓存的方法
    def get_cache(self, key):
        try:
            value_json = self.redis_client.get(key)
            # 将json数据格式转换成python字典格式
            value_dict = json.loads(value_json)
            if value_dict:
                return value_dict
            return None
        except Exception as e:
            print(f'获取缓存失败: {e}')
            return None

    # todo:5-定义删除缓存的方法
    def delete_cache(self, key):
        try:
            self.redis_client.delete(key)
            return True
        except Exception as e:
            print(f'删除缓存失败: {e}')
            return False

    # todo:6-定义清空redis库所有缓存的方法
    def flush_all_cache(self):
        try:
            self.redis_client.flushdb()
            return True
        except Exception as e:
            print(f'清空缓存失败: {e}')
            return False


# todo:7-程序入口
if __name__ == '__main__':
    # 创建缓存对象
    cache = RedisCache()
    # 测试数据
    user_data = {
        'id': 1,
        'name': '张三',
        'email': 'zhangsan@example.com',
        'last_login': '2024-01-01 10:00:00'
    }
    # 调用设置缓存的方法
    result = cache.set_cache(key='user:1', value=user_data, expire_time=300)
    print(result)

    # 获取缓存数据
    cache_data = cache.get_cache(key='user:1')
    print('cache_data--->', type(cache_data), cache_data)

    # 删除缓存数据
    cache.delete_cache(key='user:1')

