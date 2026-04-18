"""
概念: 在函数嵌套的前提下, 内部函数使用了外部函数的变量或参数, 并且外部函数返回内部函数的函数名  ->  内部函数是闭包函数
3个条件: ①函数嵌套  ②引用:内部函数使用外部函数变量或参数  ③有返回值: 外部函数返回内部函数的函数名(内存地址)
作用: ①记忆能力 或者 延长外部函数变量或参数的生命周期  ②装饰器
应用场景: 账户余额更新 -> 基于现有的金额进行调整

noncal关键字: 声明外部函数的变量或参数, 可以在内部函数中修改外部函数的变量或参数
"""


# class Student():
#     def __init__(self, age):
#         self.age = age
#
#     def set_age(self, new_age):
#         self.age += new_age
#
#
# s1 = Student(20)
# print(s1.age)
# s1.set_age(10)
# print(s1.age)
# s1.set_age(10)
# print(s1.age)


# 需求: 账户余额更新 -> 基于现有的金额进行调整
# todo:1-条件1 函数嵌套
def func_outer():
    balance = 10000000

    def func_inner(money, flag):
        # print('func_inner--->', func_inner)
        # todo:2-条件2 引用:内部函数使用外部函数变量或参数
        nonlocal balance
        if flag == 'red':
            balance += money
        elif flag == 'green':
            balance -= money
        return balance

    # todo:3-条件3 有返回值: 外部函数返回内部函数的函数名(内存地址)
    return func_inner


# 调用外部函数, 将内部函数的函数名返回给f, 此时 f=func_inner
f = func_outer()
# print('f--->', f)
print('=' * 80)
# 调用f  f()=func_inner()
result = f(3000, 'red')
print('result--->', result)
result2 = f(10000, 'green')  # 累加
print('result2--->', result2)