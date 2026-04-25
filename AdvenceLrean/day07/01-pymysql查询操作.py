"""
pymysql模块使用流程:
① 导包 import pymysql
② 创建连接对象 -> 连接数据库
③ 借助连接对象创建游标对象 -> 游标就是搬运工
④ 借助游标对象进行增删改查操作
⑤ 关闭游标对象
⑥ 关闭连接对象

无论增删改查哪个操作, 都使用commit/rollback即可
commit 和 rollback
commit -> 执行成功就提交
rollback -> 执行失败就回滚
"""

# ① 导包 import pymysql
import pymysql as pm

# ② 创建连接对象 -> 连接数据库
conn = pm.connect(
    host="localhost",
    port=3306,
    user="root",
    password='123456',
    database='db_hw1',
    charset='utf8'
)
# ③ 借助连接对象创建游标对象 -> 游标就是搬运工
cur = conn.cursor()
print('cur--->', cur)

try:
    # ④ 借助游标对象进行增删改查操作
    # query: sql语句  str类型
    row = cur.execute('select * from student')
    # row中不是直接存储的查询结果
    print(f'影响的行数是:{row}')
    # 借助cur对象中的fetchone方法获取查询结果
    # fetchone(): 获取单条数据
    data1 = cur.fetchone()
    # 返回元组类型
    print('data1--->', type(data1), data1)

    print('=' * 80)

    # 借助cur对象中的fetchmany方法获取查询结果
    # fetchmany(size=): 获取多条数据
    data2 = cur.fetchmany(size=2)  # 在前边数据基础上获取后边的数据
    print('data2--->', type(data2), data2)

    print('=' * 80)

    # 借助cur对象中的fetchall方法获取查询结果
    # fetchall(): 获取所有数据
    data3 = cur.fetchall()
    print('data3--->', type(data3), data3)

    # 提交
    conn.commit()
except Exception as e:
    print(f'报错信息: {e}')
    # 发生报错回滚
    conn.rollback()

# ⑤ 关闭游标对象
cur.close()

# ⑥ 关闭连接对象
conn.close()