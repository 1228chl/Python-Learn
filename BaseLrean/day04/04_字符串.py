num_str = '0123456789'
# 索引2到5，步长为1
print(num_str[2:5:1])
# 索引0到5，步长为1
print(num_str[0:5])
# 索引1到末尾，步长为1
print(num_str[1:])
# 打印所有字符，和直接打印没区别
print(num_str[:])
# 打印所有字符，步长为2
print(num_str[::2])
# 打印所有字符，步长为-1，相当于倒序打印
print(num_str[::-1])
# 打印索引-8到-5，步长为1
print(num_str[-8:-5])
# 从头开始打印到索引为-8的位置
print(num_str[:-8])
# 从索引为-5开始打印到末尾
print(num_str[-5:])
