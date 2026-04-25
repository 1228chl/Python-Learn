"""
需求: 获取登录界面(input)用户输入的账号和密码, 和数据库用户表真实的账号和密码进行匹配, 匹配成功显示登录成功, 否则显示登录失败
① 获取用户输入的账号和密码
② 将获取的账号和密码 传入到 sql语句中  where user=账号 and pwd=密码
③ 基于查询结果 row 进行判断 是否登录成功
"""

# ① 获取用户输入的账号和密码
username = input("请输入账号: ")
password = input("请输入密码: ")

# ② 将获取的账号和密码 传入到 sql语句中  where user=账号 and pwd=密码
import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='123456',
                       database='db_hw1')
cur = conn.cursor()
# 执行查询语句
# 此行代码传参方式会导致sql注入漏洞, 影响数据安全
# row = cur.execute(query=f'''select * from user WHERE user='{username}' AND pwd="{password}"''')
# print(f'影响了{row}行数据')

# 正确的传参方式
# %s -> 不是字符串的格式化输出操作, 是sql中防止sql注入问题的参数占位符
row = cur.execute(query='''select * from user WHERE user=%s AND pwd=%s''', args=(username, password))
print(f'影响了{row}行数据')

# ③ 基于查询结果 row 进行判断 是否登录成功
# 0是False 1是True
if row:
    print('登录成功')
else:
    print('登录失败')
