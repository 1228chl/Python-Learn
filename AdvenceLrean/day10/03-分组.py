"""
分组等同于sql中的分组, 可以实现分组聚合 以及 分组过滤
"""
import pandas as pd

# 加载数据集
df1 = pd.read_csv('data/uniqlo.csv')
print(df1)

# todo:1- 获取分组对象
# 一列分组
df2 = df1.groupby(by=['gender_group'])
print(df2)
# 多列分组
df3 = df1.groupby(by=['city', 'channel'])
print(df3)

# todo:2- 调用分组对象响应的方法
print(df2.first())
print(df2.last())
# 获取对应组的组数据
print(df2.get_group(('Male',)))

print('=' * 80)

# todo:3- 分组聚合操作
print(df2.count())  # 对所有列进行count聚合
print(df2['city'])  # 获取分组对象中的某列数据
# select 分组字段, count(列名) from 表名 group by 字段
print(df2['city'].count())
# df4 = df1.groupby(by=['gender_group'])['city'].count()
# 一列分组聚合
df4 = df1.groupby(by=['gender_group'])[['city']].count()
print(df4)
# 多列分组聚合
df5 = df1.groupby(by=['gender_group'])[['city', 'channel']].count()
print(df5)

# select 分组字段, count(列名), sum(列名), max(列名) from 表名 group by 字段
df6 = df1.groupby(by=['gender_group']).agg({'city': 'count', 'revenue': 'mean'})
print(df6)
print(df6.query('revenue>150'))

# todo:4- 分组过滤
# 获取revenue平均值大于150的组数据
# x是df对象
df7 = df1.groupby(by=['gender_group']).filter(lambda x: x['revenue'].mean() > 150)
print(df7)
# x: s对象
df8 = df1.groupby(by=['gender_group'])['revenue'].filter(lambda x: x.mean() > 150)
print(df8)
