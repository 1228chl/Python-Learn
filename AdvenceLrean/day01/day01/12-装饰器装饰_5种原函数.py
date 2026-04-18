"""
原函数是否有参, 是否有返回值  要和 装饰器的内部函数保持一致
"""


# 需求: 计算两个数的加法, 在计算前输出提示信息

# 装饰器函数
def func_outer(func_name):
    def func_inner():
        print('开始进行加法计算...')
        func_name()

    return func_inner


# 无参无返回值原函数
@func_outer
def get_sum():
    a = 10
    b = 20
    sum_result = a + b
    print(f'求和结果是:{sum_result}')


get_sum()

print('=' * 80)


# 装饰器函数
def func_outer(func_name):
    def func_inner(num1, num2):
        print('开始进行加法计算...')
        func_name(num1, num2)

    return func_inner


# 有参无返回值原函数
@func_outer
def get_sum(a, b):
    sum_result = a + b
    print(f'求和结果是:{sum_result}')


get_sum(10, 20)

print('=' * 80)


# 装饰器函数
def func_outer(func_name):
    def func_inner():
        print('开始进行加法计算...')
        sum_result = func_name()
        return sum_result

    return func_inner


# 无参有返回值原函数
@func_outer
def get_sum():
    a = 10
    b = 20
    sum_result = a + b
    return sum_result


result = get_sum()
print('result--->', result)

print('=' * 80)


# 装饰器函数
def func_outer(func_name):
    def func_inner(a, b):
        print('开始进行加法计算...')
        sum_result = func_name(a, b)
        return sum_result

    return func_inner


# 有参有返回值原函数
@func_outer
def get_sum(a, b):
    sum_result = a + b
    return sum_result


result = get_sum(10, 20)
print('result--->', result)


# 装饰器函数  -> 通用装饰器
def func_outer(func_name):
    def func_inner(*args, **kwargs):
        print('开始进行加法计算...')
        sum_result = func_name(*args, **kwargs)
        return sum_result

    return func_inner


# 不定长参数的原函数
@func_outer
def get_sum(*args, **kwargs):
    """
    :param args:  接收的是 元组类型  元组可以遍历
    :param kwargs:   接收的事 字典类型   dict.keys()  dict.values()  dict.items()
    :return:
    """
    print('args--->', args)
    print('kwargs--->', kwargs)
    sum_result = 0
    for i in args:
        sum_result += i

    for k in kwargs.values():
        sum_result += k

    return sum_result


result = get_sum(10, 20, a=30, b=40)
print('result--->', result)
