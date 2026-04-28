import pandas as pd

# 加载数据集
df = pd.read_csv('data/stock_day.csv')
print(df.head())

# 删除一些无关的列
# 根据行索引值或列名 删除行或列数据
# axis: 0->按行  1->按列
df2 = df.drop(columns=["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis=1)
print(df2.head())
print('=' * 80)

# todo:1-取值操作
# 1.1 df[列名] -> 获取一列数据
df3 = df2['open']  # s对象  一维数据
# df3 = df2[['open']]  # df对象  二维数据
print(type(df3), '\n', df3)
print('=' * 80)
# df[[列名1, 列名2, ..]]  # 获取多列数据
df4 = df2[['open', 'high']]
print(type(df4), '\n', df4)
print('=' * 80)
result = df2['open']['2018-02-26']  # 先获取s对象  然后s对象根据行索引值获取数据
print(result)

# todo:2-loc 或 iloc属性
"""
既可以下标取值 也可以切片取值
loc[行索引值, 列索引值]: 基于行索引值 或 列索引值(列名) -> 肉眼看的值, 可以是数值也可以是字符串等
iloc[行下标, 列下标]: 基于行下标 或 列下标 -> 要么0,1,2,3... 要么-1,-2,-3...
"""
print(df2.loc['2018-02-27'])  # 获取行数据
print(df2.loc['2018-02-27', 'open'])  # 获取行列数据
print(df2.loc[['2018-02-27', '2018-02-26'], ['open', 'high']])
print(df2.loc['2018-02-27':'2018-02-23', 'open':'close'])  # 切片

print('=' * 80)

print(df2.iloc[0])  # 获取行数据
print(df2.iloc[0, 0])  # 获取行列数据
print(df2.iloc[[0, 1], [0, 1]])
print(df2.iloc[:5, :3])  # 切片

# todo:3- 修改值
df2['open'] = 1  # 此列的值全部修改为1
print(df2.head())
df2['high'] = df2['high'] + 10  # s对象运算, 将运算结果再赋值给列
print(df2.head())

# todo:4- 排序
# df.sort_values(by=, ascending=)  # 列值排序
# s.sort_values(ascending=)  # 列值排序
# df/s.sort_index(ascending=)  # 行索引值排序
# 列值排序
df3 = df.sort_values('open',ascending=False)
print(df3.head(50))
df4 = df.sort_values(['open', 'high'],ascending=[True,True])
print(df4.head(50))
print(df['open'].sort_values(ascending=False).head())
# 行索引值排序
df5 = df.sort_index(ascending=True)
print(df5.head(20))
print(df['open'].sort_index(ascending=False))