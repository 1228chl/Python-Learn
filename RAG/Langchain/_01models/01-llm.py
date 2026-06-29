#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Vincent
@Time    : 2026/1/4 14:42
@File    : _01_llm.py
@Function :
langchain_community 社区版本，社区支持的模块
langchain, langchain_core 官方包
langchain_openai 第三方的包
langchain_classic 旧版的接口
"""
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url=os.getenv("TONGYI_BASE_URL"),
    api_key =os.getenv("TONGYI_API_KEY"),
    model="qwen-max",
    temperature=0
)

# llm = Tongyi(
#     api_key=os.getenv("API_KEY"),
#     base_url=os.getenv("BASE_URL"),
#     model="qwen3-max"
# )

# 全文输出
print(llm.invoke("压人是什么"))
# print(llm.invoke("你好"))

# 流式输出
# for chunk in llm.stream("坦克压人是什么感觉"):
#     print(chunk.content, end="", flush=True, sep="\n")
