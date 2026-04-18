"""
概念: 本质上就是一个闭包函数
作用: 用于装饰原函数 -> 在不改变原函数的代码基础上, 给原函数添加新的功能
4个条件: ①嵌套函数  ②引用  ③有返回值  ④增加额外的功能
应用场景: ①统计程序运行时间  ②程序重试机制(带参装饰器)  ③日志记录
好处: 多个功能之间实现解耦合  维护成本低

装饰器使用方式:
①传统方式(高阶函数 -> 一个函数名是另外一个函数的实参 或者 一个函数名是另外一个函数的返回值)
原函数名 = 外部函数名(原函数名)
原函数名()

②语法糖格式  推荐使用此方式
@外部函数名
def 原函数名():
    pass

原函数名()
"""

"""
def login(username, password):
    if username == 'admin' and password == '123456':
        return True
    else:
        return False

# 定义评论函数
def comment(username, password):
    if login(username, password) == '登录成功':
        print('登录成功')
        print('评论中...')
    else:
        print('登录失败, 请先登录')


# 定义支付函数
def payment(username, password):
    if username == 'admin' and password == '123456':
        print('登录成功')
        print('支付中...')
    else:
        print('登录失败, 请先登录')


comment('admin', '123456')
payment('admin', '12345')
"""


# 需求: 用户在评论之前  以及  支付之前  都需要先进行登录

# todo:2-定义装饰器函数
# 条件1: 函数嵌套
def check_login(func_name):  # 注意点: 只能传递一个参数, 实参是原函数的函数名
    def func_inner():
        # 条件4: 增加的额外功能
        print('登录成功, 哈哈哈...')
        # 条件2: 引用
        func_name()  # 注意点: func_name就是外部函数的实参引用  ->  原函数 comment

    # 条件3: 有返回值
    return func_inner


# todo:1-定义原函数
def comment():
    print('评论中...')


# print('comment1--->', comment)

# 传统方式调用
# 先调用装饰器的外部函数, 将外部函数的返回值(func_inner)返回给调用处, 用comment变量名接收一下
# 偷梁换柱 -> comment原函数名变量中存储的时内部函数名  comment=func_inner
comment = check_login(comment)  # comment=func_inner
# print('comment2--->', comment)

comment()  # 函数调用操作 comment=func_inner  comment()=func_inner()

print('=' * 80)


# 定义支付函数
@check_login  # @check_login 等价于 payment = check_login(payment)
def payment():
    print('支付中...')


# 调用函数
payment()  # 偷梁换柱, 此时的payment是外部函数的返回值(内部函数名func_inner)