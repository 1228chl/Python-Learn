"""
pd.concat([df1, df2, ...], axis=): 按轴对df对象进行拼接, 没有关联条件, 根据列名或行索引值相同进行拼接, 一般用于上下连接 类似于 union all
pd.merge(df1, df2, how=, on=): 有条件连接, 对左右两个df进行相应的连接 how->左 右 内 外  类似于 sql中的有条件连接
"""
import pandas as pd

# todo:1- concat拼接
df1 = pd.DataFrame(data=[[1, 2, 3, 4],
                         [4, 5, 6, 7],
                         [8, 9, 10, 11]],
                   index=['a', 'b', 'c'],
                   columns=['A', 'B', 'C', 'D'])
print(df1)
df2 = pd.DataFrame(data=[[11, 12, 13, 14],
                         [24, 25, 26, 27],
                         [38, 39, 310, 311]],
                   index=['a', 'b', 'e'],
                   columns=['A', 'B', 'D', 'F'])
print(df2)

# axis: 0->上下拼接  1->左右拼接
df3 = pd.concat(objs=[df1, df2], axis=0, join='outer')
print(df3)
df4 = pd.concat(objs=[df1, df2], axis=1, join='outer')
print(df4)
# join: inner->内连接, 保留共有的行或列  outer->外连接, 保留所有行或列
df5 = pd.concat(objs=[df1, df2], axis=0, join='inner')
print(df5)

print('=' * 80)

# todo:2- merge连接
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K3'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)

# left: 左表
# right: 右表
# how: 连接方式, 默认是inner, left, right, outer
# on: 列名, 根据列值相同进行连接
# 等同于 select * from left join right on left.key1 = right.key1
# df6 = pd.merge(left=left, right=right, how='inner', on=['key1'])
# df6 = pd.merge(left=left, right=right, how='left', on=['key1'])
# df6 = pd.merge(left=left, right=right, how='right', on=['key1'])
# on=['key1']: 列名相同
# df6 = pd.merge(left=left, right=right, how='outer', on=['key1'])

# left_on='key1', right_on='key2' -> A表的key1字段 和 B表的key2字段进行条件连接
# 等同于 select * from left full join right on left.key1 = right.key2
df6 = pd.merge(left=left, right=right, how='outer', left_on='key1', right_on='key2')
print(df6)
