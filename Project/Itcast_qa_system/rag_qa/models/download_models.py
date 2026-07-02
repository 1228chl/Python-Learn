#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Vincent
@Time    : 2026/4/26 10:55
@File    : download_models.py
@Function :
模型下载到当前文件夹
"""
try:
    from modelscope import snapshot_download
except ImportError:
    print("请安装 modelscope, pip install modelscope")

import os
import sys

models = [
    "BAAI/bge-m3",
    "BAAI/bge-reranker-v2-m3",
    "iic/nlp_bert_document-segmentation_chinese-base"
]


def download_single_model(model_id):
    """
    通用模型下载函数
    """
    print(f"🚀 正在准备下载模型: {model_id}")

    # 1. 配置基础目录 (当前脚本所在目录)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 2. 确保基础目录存在
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"📂 已创建基础目录: {base_dir}")

    # 3. 处理目录名称 - 提取模型名称（去掉命名空间前缀）
    # 例如: "BAAI/bge-m3" -> "bge-m3"
    #       "iic/nlp_bert_document-segmentation_chinese-base" -> "nlp_bert_document-segmentation_chinese-base"
    dir_name = model_id.split('/')[-1]
    local_dir = os.path.join(base_dir, dir_name)

    print(f"🎯 目标保存路径: {local_dir}")

    try:
        # 4. 执行下载
        # 直接指定完整的本地目录路径
        model_dir = snapshot_download(
            model_id,
            local_dir=local_dir,  # 直接指定下载到的完整路径
            revision="master"  # 默认下载 master 分支，如需特定版本可修改
        )

        print("-" * 30)
        print(f"✅ 下载成功！")
        print(f"📁 模型位置: {model_dir}")
        print("-" * 30)

    except Exception as e:
        print(f"❌ 下载失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    for model_id in models:
        print(f"🚀 正在准备下载模型: {model_id}")
        download_single_model(model_id)
