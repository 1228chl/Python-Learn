#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Vincent
@Time    : 2025/11/07 21:47
@File    : demo_parse_args.py
@Function :
命令行解析工具介绍
"""
import argparse

# 1. 创建解析器
parser = argparse.ArgumentParser(description="EduRAG System Main Entry Point")
# --data-processing 是一个布尔值，默认是false

# 2. 创建指定参数
parser.add_argument('--data-processing', action='store_true',
                    help='Run in data processing mode instead of query mode.')
parser.add_argument('--data-dir', type=str, default='./data/ai_data',
                    help='Path to the data directory.')
parser.add_argument("-n", "--batch_size", type=int, default=8, help="指定batch size")
parser.add_argument("-lr", "--learning_rate", type=float, default=2e-5, help="指定learning rate")
parser.add_argument("-e", "--epochs", type=int, default=3, help="指定训练轮数")
parser.add_argument("--output", help="指定输出路径")
# uv venv --python python3.10
# 3. 解析参数
args = parser.parse_args()
print(args)

print(args.data_processing)
print(args.data_dir)
print(args.batch_size)
print(args.learning_rate)
