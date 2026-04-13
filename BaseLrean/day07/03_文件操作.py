"""
文件操作: 为了持久化(保存)数据, 读写操作
     基本语法: f = open(文件路径, 模式[w写, r只读, a追加])  # 路径可以是绝对路径(从盘符或者根目录/开始的路径),
                                    可以是相对路径(./相对于当前文件的当前文件夹路径, ../相对于当前文件的上一级文件夹路径)
            f.read() 读取,   f.write() 写入, 最终操作完, 需要f.close()关闭文件
"""

# 创建并写入一个简单文件
# # w: 覆写模式
# f = open("test.txt", "w", encoding="utf-8")  # 创建文件并返回文件对象  test.txt 相当于 ./test.txt
# f.write("hello world")  # 写入数据
# """
# # 在Windows默认写入字符集是ANSI(gbk), pycharm默认识别是utf-8字符集, 可以使用encoding="utf-8"参数防止乱码
# 还有个常用的字符集, 最基础的字符集 ASCII (数字, 英文..), gbk(Windows下的编码字符, 包含中文), utf-8(具有所有人类语言编码集)
# """
# f.write("\n人生苦短, 我学python")
# f.close()  # 关闭文件

# # a: 追加模式
# f = open("test.txt", "a", encoding="utf-8")
# f.write("\n追加模式")
# f.write("\n人生苦短, 我学python")
# f.close()

# r: 只读模式
# f = open("test.txt", "r", encoding="utf-8")
# 1. read()方法读取
# # print(f.read())  # 读取文件所有内容
# # print(f.read(10))  # 读取指定字符数
# # print(f.read(10))  # 在之前读取的位置继续向后读取
# while True:  # 循环读取所有文件内容, (文件很大, 指定字符分批读取)
#     content = f.read(10)
#     if not content:
#         break
#     print(content)

# 2. readline()方法读取
# line = f.readline()  # 每次读取一行数据
# print(line)
# line = f.readline()  # 接着上次向后读取一行数据
# print(line)
# while True:  # 循环读取所有文件内容, (文件很大, 指定字符分批读取)
#     content = f.readline()
#     if not content:
#         break
#     print(content)

# 3. readlines()方法读取
# li = f.readlines()  # 读取所有行数据, 返回一个列表, 每行数据是一个元素
# print(li)
# for line in li:
#     print(line)
# f.close()

with (open("G:/file/04_代码/python_project/day07/01_函数参数.py", mode='r', encoding="utf-8") as f ,
      open("04_de.py", mode='a', encoding="utf-8") as f1):
    for line in f:
        f1.write(line)


