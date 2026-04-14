"""
装饰器：是闭包的特例，需要满足闭包的条件（闭包定义：有嵌套，有引用，有返回）
    场景：增强被装饰的函数（给装饰的函数增加功能）
"""
import time


# 创建装饰器
def decorator(func):
    def wrapper():
        print("登录")
        func()
        print("登出")
    return wrapper

def comment():
    print("评论")

def download():
    print("下载")

f = decorator(comment)
f()
f = decorator(download)
f()

@decorator
def comment():
    print("评论")
@decorator
def download():
    print("下载")

comment()
download()


def get_time(fn):
    def inner():
        # 添加装饰器修饰功能（获取程序的执行时间）
        begin = time.time()
        # 调用fn函数，执行原函数代码
        fn()
        end = time.time()
        print(f"这个函数的执行时间：{end-begin}")
    return inner

@get_time
def demo():
    for i in range(100000000):
        print(i)

demo()

# 实现一个打印日志的装饰器，被装饰的函数是带参的
def logging(func):
    def wrapper(*args, **kwargs):
        print(f"日志信息：{func.__name__}开始执行")
        func(*args, **kwargs)
        print(f"日志信息{func.__name__}结束执行")
    return wrapper

@logging
def sum_num(*args,**kwargs):
    # 初始化保存结果的变量
    result = 0
    # 累加kwargs参数
    result += sum(args)
    # 累加kwargs参数
    result += sum(kwargs.values())
    return result
sum_num(1,2,3,4,a=1,b=2,c=3,d=4,e=5)

# 实现装饰带返回值的函数的装饰器
# 实现一个打印日志的装饰器，被装饰的函数是带参的
def logging(func):
    def wrapper(*args, **kwargs):
        print(f"日志信息：{func.__name__}开始执行")
        r = func(*args, **kwargs)
        print(f"日志信息{func.__name__}结束执行")
        return r
    return wrapper

@logging
def sum_num(*args,**kwargs):
    # 初始化保存结果的变量
    re = 0
    # 累加kwargs参数
    re += sum(args)
    # 累加kwargs参数
    re += sum(kwargs.values())
    return re
res = sum_num(1,2,3,4,a=1,b=2,c=3,d=4,e=5)
print(res)

print("*"*50)
# 实现装饰器本身传参
def logging(flag):
    def docorator(func):
        def wrapper(*args, **kwargs):
            if flag == "info":
                print(f"日志信息{func.__name__}开始执行")
            if flag == "warn":
                print(f"警告信息{func.__name__}开始执行")
            result = func(*args, **kwargs)
            if flag == "info":
                print(f"日志信息{func.__name__}结束执行")
            if flag == "warn":
                print(f"警告信息{func.__name__}结束执行")
            return result
        return wrapper
    return docorator

@logging("info")
def sum_num(*args,**kwargs):
    # 初始化保存结果的变量
    result = 0
    result += sum(args)
    result += sum(kwargs.values())
    return result

result = sum_num(1,2,3,4,a=1,b=2,c=3,d=4,e=5)
print(result)

print("*"*50)

@logging("warn")
def sum_num(*args,**kwargs):
    re = 0
    re += sum(args)
    re += sum(kwargs.values())
    return re
result = sum_num(1,2,3,4,a=1,b=2,c=3,d=4,e=5)
print(result)