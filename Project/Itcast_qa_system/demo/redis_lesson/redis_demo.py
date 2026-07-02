#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Vincent
@Time    : 2026/6/19 18:22
@File    : redis_demo.py
@Function :
"""
import json

import redis


def demo1():
    # decode_responses=False
    client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    client.set('name', 'Vincent')
    print(client.get('name'))

    # decode_responses=True
    client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    client.set('name', 'Vincent')
    print(client.get('name'))


def demo2():
    # redis 支持hash数据结构
    client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    client.hset("query:python如何安装包？",
                mapping={"query": "python如何安装包？", "answer": "使用pip install 包名 来安装"})
    print(client.hget("query:python如何安装包？", "answer"))
    # print(client.hget("query:python如何安装包？", "query"))
    print(client.hgetall("query:python如何安装包？"))


def demo3():
    import time
    # 设置过期时间
    client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    client.set("username", json.dumps({"name": "Vincent", "age": 25}))
    print(client.get("username"))
    # client.setex("username", 5, "Vincent")
    client.set("username", "Vincent", ex=5)
    time.sleep(6)
    print(client.get("username"))  # 返回None

    # client.incr("username")
    # client.expire("username", 5)


def demo4():
    import time
    # 限流计数器
    # 限制在某个时间段内，限制请求次数
    client = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def is_allowed(user_id, limit=5, window=10):
        key = f"limit:{user_id}"
        # 原子自增
        count = client.incr(key)
        # print("count:", count)
        # 第一次请求，设置过期时间
        if count == 1:
            client.expire(key, window)
        return count <= limit

    # 测试
    for i in range(10):
        print(i, is_allowed("user_1"))

    for i in range(10):
        if i == 5:
            time.sleep(10)
        print(i, is_allowed("user_2"))


if __name__ == '__main__':
    demo4()
