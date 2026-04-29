import pandas as pd

data = {
    '性别': ['男', '女', '男', '女', '男', '女', '女', '男'],
    '购买': ['是', '否', '是', '是', '否', '否', '是', '否']
}
# 创建df对象
df1 = pd.DataFrame(data)
print(df1)

# todo:1- 交叉表
# index: 行索引值的分组字段
# columns: 列索引值的分组字段
df2 = pd.crosstab(index=df1['性别'], columns=df1['购买'])
print(df2)
df3 = df1.groupby(by=['性别', '购买'])['购买'].count()
print(df3)

print('=' * 80)

# todo:2- 透视表
data = {
    '性别': ['男', '女', '男', '女', '男', '女'],
    '购买': ['是', '否', '是', '是', '否', '否'],
    '金额': [100, 150, 200, 130, 160, 120]
}
df = pd.DataFrame(data)
print(df)

# 统计不同性别不同购买情况的平均金额
# as_index: 重置行索引值
df1 = df.groupby(by=['性别', '购买'], as_index=False)[['金额']].mean()
print(df1)
# index: 行索引值的分组字段
# columns: 列索引值的分组字段
# valuess: 统计值的字段
# aggfunc: 统计函数, 默认是mean
df2 = pd.pivot_table(data=df, index=['性别'], columns=['购买'], values=['金额'], aggfunc='mean')
print(df2)
