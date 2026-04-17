# 回顾：全局作用域定义的变量就是全局变量，局部作用域定义的变量是局部变量

# 局部作用域可以访问局部变量，全局作用域可以访问全局变量
# 全局作用域
# num1 = 10 # 全局变量
# def fun1():
#     # 局部作用域
#     num2 = 20
#     print(num2)
# fun1()
# print(num1)
#
# # 局部作用域可以访问全局变量
# # 全局作用域
# num1 = 10  # 全局变量
# def fun1():
#     # 局部作用域
#     num2 = 20  # 局部变量
#     print(num1)
#
# fun1()
#
# # 局部作用域同名赋值的变量会覆盖全局作用域的同名变量
# num1 = 10 # 全局变量
# def fun1():
#     # 局部作用域
#     num1 = 20# 局部变量
#     print(num1)
# fun1()
# print(num1)
#
# # 局部作用域想要修改全局变量, 需要使用global关键字声明变量
# # 全局作用域调用局部变量, 需要使用global关键字声明变量
# num1 = 10# 全局变量
# def fun1():
#     # 局部作用域
#     global num1 # 局部变量
#     num1 = 20
#     print(num1)
# fun1()
# print(num1)


# 定义闭包
def func():
    num = 10
    def inner():
        # 引用num变量
        print(num)
    # 返回了内部函数的名称（内存地址）
    return inner
f = func()
print(f)
f()

print("*" * 40)
# 闭包，内部函数如果要修改外部函数的变量，需要使用nonlocal关键字声明变量
def func():
    num = 10
    def inner():
        num = 20
        print("n",num)
    print("w",num)
    inner()
    print("w",num)
    return inner
f = func()
f()

print("*" * 40)
def func():
    num = 10
    def inner():
        nonlocal num
        num = 20
        print("n",num)
    print("w",num)
    inner()
    print("w",num)
    return inner
f = func()
f()

# 闭包案例：带参的闭包，实现数值累加
# 闭包的使用场景：实现携带记忆状态的功能（闭包 + 引用外部函数作用域的参数（作为记忆状态））
def func():
    # 初始化累加初始值
    result = 0
    def inner(num,flag):
        nonlocal result
        if flag == 'red':
            result += num
            print("n",result)
        elif flag == 'green':
            result -= num
            print("n",result)
    return inner

f = func()
f(1,'red')
f(2,'green')
f(3,'red')

