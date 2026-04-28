import pandas as pd

# 加载数据集
df = pd.read_csv('data/stock_day.csv')

# 删除一些无关的列
# 根据行索引值或列名 删除行或列数据
# axis: 0->按行  1->按列
df2 = df.drop(columns=["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis='columns')
print(df2.head())

# todo:1- 算法运算
# 借助add() sub() mul() div() 方法对s对象进行计算

result1 = df2['open'].add(1)
print(result1)

# 列和列之间运算  参考mysql的字段之间运算
# result2 = df2['open'].add(other=df2['high'])
result2 = df2['open']+df2['high']
print(result2)

# round(): 保留小数点后n位, 四舍五入
result3 = (df2['open']+df2['high']).round(1)
print(result3)
print(df2['open'].round(1))
# df2['open'] = np.floor(df2['open'])
# print(df2.head())

print('==' * 80)

# todo:2- 逻辑运算
# select name, age from 表名  ->  df[[name, age]]  获取列
# 模拟mysql中where进行过滤条件获取满足条件的行数据
print(df2['open'] > 23)# 返回bool类型的s对象
result4 = df2[df2['open'] > 24]# 1个条件
print(result4)
result5 = df2[(df2['open'] > 23) & (df2['open'] < 25)]# 2个条件  &->and
print(result5)
result6 = df2[(df2['open'] < 23) | (df2['open'] > 26)]# 2个条件  |->or
print(result6)
result7 = df2[~(df2['open'] < 23) | (df2['open'] > 26)]# ~->not
print(result7)

# query()
# result8 = df2.query('open>23')
# result8 = df2.query('open>23 & open<25')
result8 = df2.query('open < 23 | open > 25')
print(result8)

# isin(): 判断列值是否在指定的列表数据中, 返回bool值类型的s对象
print(df2['open'].isin([23.53,22.80]))

# 基于bool值s对象进行过滤, 获取满足条件的行数据
result9 = df2[df2['open'].isin([23.53,22.80])]
print(result9)
