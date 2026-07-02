#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Vincent
@Time    : 2026/4/20 10:00
@File    : _logger.py
@Function :
"""
import logging
import os


def setup_logger(name, log_file='logs/app.log'):
    # 确保日志目录存在
    print(os.path.dirname(log_file))
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # 设置最低级别

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 创建文件处理器
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(logging.DEBUG)

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    # 设置处理器格式
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 添加处理器（避免重复添加）
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger("example5")


def process_data(data):
    logger.debug(f"开始处理数据: {data}")
    if not data:
        logger.error("数据为空，无法处理")
        return None
    logger.info("数据处理完成")
    return data.upper()


def main():
    logger.info("程序启动")
    result = process_data("hello")
    if result:
        logger.info(f"处理结果: {result}")
    else:
        logger.warning("处理失败")
    logger.info("程序结束")


if __name__ == "__main__":
    main()
