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

# ✅ 必须使用事务的场景
- 多表关联写入（转账、订单处理）a
- 先查后改（库存扣减、预订系统）
- 批量操作的一致性
- 外键级联操作
- 需要部分回滚的复杂逻辑

# ❌ 不需要事务的场景
- 单条记录的简单插入
- 纯SELECT查询
- 数据库结构变更（DDL）
- 日志记录（可以容忍偶尔失败）
"""

# ① 导包 import pymysql
import pymysql

# ② 创建连接对象 -> 连接数据库
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='123456',
                       database='db_hw1')
print('conn--->', conn)

# ③ 借助连接对象创建游标对象 -> 游标就是搬运工
cur = conn.cursor()
print('cur--->', cur)

try:
    # ④ 借助游标对象进行增删改查操作
    # todo: 增加数据 插入数据
    # query: sql语句  str类型
    # row = cur.execute(query='INSERT INTO GOODS(NAME, CATE_NAME, BRAND_NAME) VALUES ("测试", "测试", "测试");')
    # todo: 修改数据
    # row = cur.execute(query="""update goods set name='测试111' WHERE id=23;""")
    # todo: 删除数据
    row = cur.execute(query="delete from student WHERE id=11;")
    # row中不存储插入数据的结果, 只存储sql语句执行成功返回的受影响的行数
    print(f'影响的行数是:{row}')
    # print(1 / 0)
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
