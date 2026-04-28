"""
series对象是pandas中最基础的数据结构, dataframe对象是由多个series对象组成
df对象中的一行或一列数据就是一个series对象
series对象可以看做是一维数据
"""
import pandas as pd
import numpy as np

# todo:1- 创建series对象
"""
pd.Series(data=, index=)
data: 数据  可以是list tuple dict ndarray类型
index: 索引  设置s对象的索引值
"""
# 不手动设置索引值, 默认从0开始
s1 = pd.Series(data=[1, 2, 3, 4])
print('s1--->', type(s1), '\n', s1)
s2 = pd.Series(data=(1, 2, 3, 4))
print('s2--->', type(s2), '\n', s2)
s3 = pd.Series(data=[1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
print('s3--->', type(s3), '\n', s3)
# key是s对象的索引值, value是s对象的数据值
s4 = pd.Series(data={'A': 1, "B": 2, "C": 'a'})
print('s4--->', type(s4), '\n', s4)
s5 = pd.Series(data=np.arange(5))
print('s5--->', type(s5), '\n', s5)

# todo:2- s对象的属性
# s对象中数据的类型
print('s5.dtype--->', s5.dtype)
print('s5.dtypes--->', s5.dtypes)

# s对象的索引值
print('s3.index--->', s3.index)
print(s3.index[0])

# s对象的数据
print('s5.values--->', type(s5.values), s5.values)

# s对象的形状
print(s5.shape)

# 根据索引值获取对应的数据值
print(s3['A'])
print(s3.A)  # 对象名.属性名