# eg: 女孩子在头上带头饰, 可以带一个, 也可以带多个  -> 原函数增加多个额外功能
"""
多个装饰器装饰一个原函数:
语法糖方式: 根据人类的理解, 从上往下加糖  先进入登录界面登录, 然后进行验证码校验
传统方式: 由内到外(先添加哪个额外功能, 此额外功能装饰器函数就要挨着最终的函数调用)  -> 实际的代码执行流程
"""
from decorator import check_login, check_code


# 定义原函数
@check_login
@check_code
def comment():
    print('评论中...')


comment()

print('=' * 80)


def payment():
    print('支付中...')



# 传统方式调用
# payment = check_code(payment)
# payment = check_login(payment)
# payment()

cc = check_code(payment)  # 外

cl = check_login(cc)  # 内

cl()
