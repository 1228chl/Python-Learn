#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Vincent
@Time    : 2026/6/22 11:13
@File    : demo.py
@Function :
"""
from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)
client.fput_object("edurag", "demo.py", "./demo.py")
client.fget_object("edurag", "价格1.png", "./price.png")
print(client.list_objects("edurag"))
