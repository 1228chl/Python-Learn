print("hello")
print("hello")
print("hello")
print("hello")

def say_hello():
    print("hello")

say_hello()
say_hello()
say_hello()
say_hello()
print(say_hello())

def my_sum(a,b):
    print(a+b)

my_sum(1,2)
my_sum(3,2)

def get_sum(a,b):
    return a+b

res = get_sum(1,2)
print(res)

def get_calc(a,b,c):
    temp_sum = a+b+c
    temp_mul = a*b*c
    return temp_sum,temp_mul

res = get_calc(2,2,3)
print(res)
print(type(res))

def outer_func():
    print("这是调用了外部函数")

def temp_func():
    print("这是当前函数的执行逻辑")
    outer_func()
    print("这是当前函数的结束逻辑")
    return "这是当前函数的返回值"

res = temp_func()
print(res)

numbers_list = [1,23,3,24,2,1,2,4,15,43,564,323,4,43,342,3]

def calculate_sum(nl):
    j_ans = 0
    o_ans = 0
    for i in nl:
        if i % 2 == 0 :
            o_ans += i
        else:
            j_ans += i
    return [o_ans,j_ans]

print(calculate_sum(numbers_list))