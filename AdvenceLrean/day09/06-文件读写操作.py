import pandas as pd


# todo:1- csv格式
# csv文件本质上是文本文件(数据之间默认分隔符是逗号, 可以自己修改), 在windows系统中可以使用excel打开
# 加载
df1 = pd.read_csv(filepath_or_buffer='data/stock_day.csv')
print(df1.head())
df2 = pd.read_csv(filepath_or_buffer='data/stock_day.csv', usecols=['open', 'high'], sep=',')
print(df2.head())
# 保存
# index: 是否保存行索引值, 默认True
# header: 是否保存列索引值, 默认True
# sep: 保存数据的分隔符, 默认是逗号
# mode: 默认是w->覆盖/重写, 如果是a->追加
df2.to_csv('data/new_stock_day.csv', index=False, header=False, sep=':', mode='w')

# todo:2- json格式
# lines: 是否按行读取数据, 默认False
df3 = pd.read_json(path_or_buf='data/Sarcasm_Headlines_Dataset.json', lines=True)
print(df3)

# lines: 默认False, 将所有数据按1行存储
df3.to_json('data/new_Sarcasm_Headlines_Dataset.json')
df4 = pd.read_json(path_or_buf='data/new_Sarcasm_Headlines_Dataset.json', lines=False)
print(df4)

# todo:3- mysql数据库
"""
需要安装以下两个模块
pip install pymysql==1.1.2 -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install sqlalchemy==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple/
"""
# 读取csv文件数据
# df5 = pd.read_csv('data/csv示例文件.csv', encoding='gbk', usecols=['birthday', 'name', 'AKA'])
# print(df5)
# df5.info()
# # 创建数据库连接引擎
# from sqlalchemy import create_engine
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/my_db?charset=utf8')
# # 存储到数据库
# # name: 表名, 表不存在会自动创建
# # con: 数据库连接引擎
# # index: 是否保存行索引值, 默认True
# # if_exists: 表存在时, 默认是fail->报错, 如果是replace->覆盖, 如果是append->追加
# df5.to_sql(name='csv_table', con=engine, index=False, if_exists='replace')
#
# # 读取数据库的表数据
# df6 = pd.read_sql(sql='csv_table', con=engine)
# print(df6)

# df7 = pd.read_sql(sql='select * from csv_table', con=engine)
# print(df7)