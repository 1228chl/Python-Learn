"""
编码:
将字符串类型(str)转换成二进制类型(bytes)  人话:将人类能看懂的数据转换成计算机能看懂的数据
str.encode(码表)  码表->utf-8 或 gbk

解码:
将二进制类型(bytes)转换成字符串类型(str)  人话:将计算机能看懂的数据转换成人类能看懂的数据
bytes.decode(码表)  码表->utf-8 或 gbk

utf-8: 1个中文3个字节    1个英文 数字 符号 都是1个字节
gbk: 1个中文2字节    1个英文 数字 符号 都是1个字节

如果发生报错或者是乱码问题, 一定是utf-8或者gbk选择有问题

扩展:
1GB=1024MB
1MB=1024KB
1KB=1024bytes  字节
1bytes=8bit   比特

当前说的7B模型, 如何计算加载此模型时需要多少GB的显存?
7B -> B十亿 70亿个数值  确定数值是什么类型(float32/float16/int8/int4)
float32/float16/int8/int4 -> 32/16/8 指的就是bit(比特)
例如: 7B模型的数值的类型是 float32, 一个数值占用多少字节bytes  32/8=4个字节
7 * 10^9 * 4 / 1024 / 1024 / 1024 ≈ 7 * 4 ≈ 28GB显存
"""

# 定义字符串类型数据
str1 = '特朗不靠谱'
# todo：编码
# encoding：码表，默认是utf-8
bytes_data_utf8 = str1.encode('utf-8')
print(bytes_data_utf8)
bytes_data_gbk = str1.encode('gbk')
print(bytes_data_gbk)
print("*"*80)

# todo: 解码
str_data_utf8 = bytes_data_utf8.decode('utf-8')
print(str_data_utf8)
str_data_gbk = bytes_data_gbk.decode('gbk')
print(str_data_gbk)