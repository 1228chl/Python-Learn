"""
df对象可以看做是二维数据, 有行有列, 类似于excel或mysql表数据 -> 结构化数据
"""
import pandas as pd
import numpy as np

# todo:1-创建df对象
"""
pd.DataFrame(data=, columns=, index=, dtype=)
data: 数据 dict list tuple ndarray
columns: 列索引值(列名)
index: 行索引值
"""
# 1.1 基于字典数据创建
dict_data = {
    '日期': ['2021-08-21', '2021-08-22', '2021-08-23'],
    '温度': [25, 26, 50],
    '湿度': [81, 50, 56]
}
# key是列索引值, value是数据值, 不设置行索引值有默认值从0开始
df1 = pd.DataFrame(data=dict_data)
print('df1--->', type(df1), '\n', df1)

# 1.2 基于列表嵌套, 元组嵌套创建  二维数据
# df2_data = [
#     ('2021-08-21', 25, 81),
#     ('2021-08-22', 26, 50),
#     ('2021-08-23', 27, 56)
# ]
# df2_data = [
#     ['2021-08-21', 25, 81],
#     ['2021-08-22', 26, 50],
#     ['2021-08-23', 27, 56]
# ]
df2_data = (
    ('2021-08-21', 25, 81),
    ('2021-08-22', 26, 50),
    ('2021-08-23', 27, 56)
)
# df2 = pd.DataFrame(data=df2_data)
# 设置行列索引值
df2 = pd.DataFrame(data=df2_data, index=['row1', 'row2', 'row3'], columns=['日期', '温度', '湿度'])
print('df2--->', type(df2), '\n', df2)

# 1.3 基于数组创建
arr_data = np.random.randint(low=0, high=101, size=(10, 5))
index = ['同学' + str(i) for i in range(10)]
columns = ['语文', '数学', '英语', '物理', '化学']
df3 = pd.DataFrame(data=arr_data, columns=columns, index=index)
print('df3--->', type(df3), '\n', df3)

# todo:2-df的属性
print('=' * 80)
print(df3.index)  # 行索引值
print(df3.columns)  # 列索引值
print(df3.values)  # 返回二维数组
print(df3.shape)  # 形状 (行数, 列数)
print(df3.dtypes)  # 查看每列的数据类型
print(df3.size)  # 元素值个数
print(df3.ndim)  # 维度数
print(df3.T)  # 转置

# todo:3-df的方法
print('=' * 80)
print(df3.head())  # 默认查看前5行数据
print(df3.head(n=2))
print(df3.tail())  # 默认查看后5行数据
print(df3.tail(n=3))

# todo:4-df的索引操作
# 修改行列索引值
df3.index = ['row_' + str(i) for i in range(10)]
df3.columns = ['column_' + str(i) for i in range(5)]
print(df3)
# 修改指定的行列索引值
# inplace: 是否修改原对象, 默认False
# columns/index: 接收dict类型 {原索引值: 新索引值}
df3.rename(columns={'column_0': '语文', 'column_1': '数学'}, index={'row_0': '同学1', 'row_1': '同学2'}, inplace=True)
# df3 = df3.rename(columns={'column_0': '语文', 'column_1': '数学'}, index={'row_0': '同学1', 'row_1': '同学2'})
print(df3)

print('=' * 80)
# 重置行索引值
# drop: 是否删除原索引值, 默认False->将原索引值作为新的列
df3 = df3.reset_index(drop=True)
print(df3)

print('=' * 80)
# 设置列值作为行索引值
df4 = pd.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale': [55, 40, 84, 31]})
print(df4)
# keys: 接收列名列表, 将指定的列值设置为行索引值
# df5 = df4.set_index(keys=['month'])
df5 = df4.set_index(keys=['month', 'year'])
print(df5)

