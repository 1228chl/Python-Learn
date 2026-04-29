"""
pandas中的缺失值来自于numpy, 用NaN表示, 没有任何含义
查看缺失值: isnull()  notnull()  info()
处理缺失值: dropna()->删除(缺失值数量非常多,一般不建议删除,导致信息丢失)  fillna()->填充
特殊情况: ?/*等其他特殊符号表示缺失值 -> 先替换(replace)成NaN, 再进行处理
"""
import pandas as pd
import numpy as np

# 加载数据集
df1 = pd.read_csv('data/movie.csv')
print(df1.head())

# todo:1-查看是否有缺失值
df1.info()
# 返回True或False,  True:有缺失值
print(df1.isnull())
print(df1.isna())
# 返回True或False,  False:有缺失值
print(df1.notnull())
print(df1.notna())
# df1.notna()-> False表示缺失值
# np.all() -> 全为True才返回True  如果返回False就说明数据集中存在缺失值
print(np.all(df1.notna()))

print('=' * 80)

# todo:2-统计缺失值个数
# 按列统计缺失值个数
print(df1.isnull().sum())
# 按行统计缺失值个数
print(df1.isnull().sum(axis=1))

print('=' * 80)

# todo:3-处理缺失值
# 删除  一般不建议删除, 会导致信息丢失
# axis: 0->按行  1->按列
df2 = df1.dropna()
df2.info()
df3 = df1.dropna(axis=1)
df3.info()

# 填充
df4 = df1.fillna(value=0)  # 填充常数
df4.info()
print(df4['Revenue (Millions)'])

print('=' * 80)

# print(df1['Revenue (Millions)'].mean())
# df1['Revenue (Millions)'] = df1['Revenue (Millions)'].fillna(df1['Revenue (Millions)'].mean())
# df1.info()
# print(df1['Revenue (Millions)'])

print('=' * 80)
# 循环遍历每列进行缺失值填充
print(df1.columns)  # 获取列名列表
print(df1[df1.columns[0]])  # 列表下标取值, 获取对应的列名  df[列名]
for column in df1.columns:
    print(column)
    # 如果条件成立, 说明此列存在缺失值
    if not np.all(pd.notnull(df1[column])):
        df1[column] = df1[column].fillna(df1[column].mean())

df1.info()
