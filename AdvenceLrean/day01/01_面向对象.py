# # defined class
# class Person(object):
#     # defined property
#     name = "zhangsan"
#     age = 18
#     # defined method
#     def speak(self):
#         print(f"hello {self.name}")
#     def eat(self):
#         print(f"{self.name} eat")
#
# p = Person()
# p.speak()
# p.eat()
# print(p.name)
# print(type(p.name))

# # self参数：代表当前对象，self参数必须放在第一个参数位置
# class Person(object):
#     # name = "zhangsan"
#     # age = 18
#
#     # defined method
#     def speak(self):
#         print(f"hello {self.name},my age is {self.age}")
#     def eat(self):
#         print(f"{self.name} eat")
#     def day_work(self):
#         self.speak()
#         self.eat()
#
# # 创建对象
# p1 = Person()
# p1.name = "张三"
# p1.age = 20
# p1.speak()
# p1.eat()
#
# p2= Person()
# p2.name ="lis"
# p2.age = 30
# print(p2.name)
# p2.speak()
# p2.eat()
# p2.day_work()
#
# # 拓展：os模块（操作文件的模块）
# import os
# print(os.getcwd())
# print(os.path.join(os.path.dirname(__file__),"__init__.py"))
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# # 魔法方法：类内定义特殊方法，使用__方法名__包裹的方法
# # __init__：初始化方法（构造方法），类实例化的时候会自动调用
# class Person(object):
#     # 构造方法
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     # 定义方法
#     def speak(self):
#         print(f"hello {self.name},my age is {self.age}")
#
#     def eat(self):
#         print(f"{self.name} eat")
#
#     def day_work(self):
#         self.speak()
#         self.eat()
#
# # 类接收的变量是直接传给构造方法，构造方法第一个参数self是会自动传入，不需要手动传参
# p1 = Person("张三",18,"男")


# __str__:魔术方法，描述对象
class Car(object):
    # 构造方法
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price

    # 描述对象
    def __str__(self):
        return f"汽车品牌：{self.brand}，汽车颜色{self.color}，汽车价格{self.price}"

c1= Car("保时捷","black",1000000)
print(c1)# 在没有str方法，默认打印对象的内存地址
print(c1)# 这会执行str方法，进行一个输出

# del 魔术方法，常用来关闭文件或者关闭数据库连接
class FileOperator:
    def __init__(self,file_path):
        self.f = open(file_path,"w",encoding="utf-8")

    def write(self,content):
        self.f.write(content)

    def close(self):
        self.f.close()

    def __del__(self):
        self.close()

file = FileOperator("test.txt")