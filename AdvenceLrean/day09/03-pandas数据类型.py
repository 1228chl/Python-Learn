"""
数据类型:
object: 字符串类型
int: 整数类型 int8/16/32...
float: 小数类型 float16/32/...
bool: 布尔值类型
datetime: 日期时间类型
timedelta: 时间差类型
category: 分类类型
nan: 空值类型

本质是列数据的类型
"""
import pandas as pd

dict_data = {
    '日期': ['2021-08-21', '2021-08-22', '2021-08-23'],
    '温度': [25, 26, 50],
    '湿度': [81, 50, 56]
}

df1 = pd.DataFrame(dict_data)
print('df1--->', df1)
# 查看列数据的类型
print(df1.dtypes)
# info(): 对象类型 行索引 列数统计 每列信息(列名 是否有null值 列类型) 不同类型的列数  数据占用内存大小
df1.info()

df1['温度'] = df1['日期'].astype('datetime64[ns]')
print(df1.dtypes)
print(df1)

# 修改列数据类型
# 获取列 -> df[列名]
# df1['温度'] = df1['温度'].astype(np.int16)
# df1['日期'] = df1['日期'].astype('datetime64[ns]')  # 日期时间类型
df1['日期'] = pd.to_datetime(df1['日期'],format='%Y-%m-%d')
print(df1.dtypes)
print(df1)

# 时间差类型
start_date= pd.to_datetime('2023-09-01')
end_date= pd.to_datetime('2024-09-30')
diff_date= end_date - start_date
print(type(diff_date),diff_date)

# 分类类型
s1 = pd.Series(['上海','北京','深圳'],dtype='category')
print(s1)