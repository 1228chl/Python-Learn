def fun1():
    print("this ordinary functions")

fun1()
fun2 = lambda : print("this anonymous function")
print(fun2)
print(fun2())

# 匿名函数
fun3 = lambda : 100
print(fun3)

fun4 = lambda a,b: a+b
print(fun4(1,2))

fun5 = lambda a,b=10:a+b
print(fun5(1))
print(fun5(2,3))

fun6 = lambda a,b : a+b if a>b else b-a
print(fun6(6,2))
print(fun6(2,3))

students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
students.sort(key=lambda x: x['age'] * 2)  # x 表示 students列表中的元素, 也就是每一行的数据(每个字典元素)
print(students)



