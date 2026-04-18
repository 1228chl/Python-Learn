"""
带参数的装饰器 也可以叫做 装饰器函数工厂
"""

# 需求：根据用户传入的flag标识，选择 提示加法计算 还是 减法计算

# 装饰器函数
def create_decorator(flag):
    def func_outer(func_name):
        def func_inner():
            if flag == '+':
                print("开始进行加法计算。。。")
            elif flag == '-':
                print("开始进行减法计算。。。")
            func_name()
        return func_inner
    return func_outer

# 定义原函数
@create_decorator('+')
def get_sum():
    a=10
    b=20
    result = a + b
    print(result)

get_sum()