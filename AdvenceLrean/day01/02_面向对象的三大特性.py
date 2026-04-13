"""
面向兑现的三大特性：封装，继承，多态
    封装：1.用类封装实体的属性和方法
         2.封装私有属性或私有方法，限制外部直接访问
    私有属性定义：__属性名 = 属性值
        一般为了操作私有属性，会对外公开 公有的接口
        获取私有属性方法：get_属性名()
        设置私有属性方法：set_属性名()
"""


# #创建类
# class Person:
#     def __init__(self, name ,age):
#         self.name = name
#         self.__age = age
#         self._height = 180
#
# # 创建对象
# p1 = Person("张三",18)
# print(p1.name)
# print(p1._height)
# # # 私有属性禁止在类外直接访问
# # print(p1.__age)
# # # 私有属性可以通过 类名._类名__属性名 访问
# # # （python对私有属性留的后门, 可以绕过私有属性进行访问)
# # print(p1._Person__age)
# # 如果需要对外公开访问权限, 一般使用get_属性名() 和 set_属性名() 方法
# class Person:
#     def __init__(self, name ,age):
#         self.name = name
#         self.__age = age
#         self._height = 180
#     # 公开获取属性
#     def get_age(self):
#         return self.__age
#     # 公开设置属性
#     def set_age(self,age):
#         self.__age = age
#
# p1 = Person("张三",18)
# print(p1.name)
# print(p1.get_age())
# p1.set_age(20)
# print(p1.get_age())
#
# print("--"*40)

# # 在暴露共有方法时，可以 校验参数格式，或者校验调用权限等，对外部进行有限访问的控制
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#         self._height = 180
#     # 公开获取属性
#     def get_age(self):
#         if self.name == "张三": # 用户权限校验
#             return f"获取私有属性age的值：{self.__age}"
#         return "无权访问"
#
#     # 公开设置属性
#     def set_prop(self, name, age):
#         print(f"设置私有属性 age 的值: {age}")
#         # isinstance(变量, 类型), 判断变量是否是指定类型, 如果是的话, 返回True, 否则返回False
#         if isinstance(name, str):
#             self.name = name
#         if isinstance(age, int):
#             if 0 <= age <= 120:
#                 self.__age = age
#
# p1 = Person('张三',18)
# print(p1.get_age())
# p1.set_prop('李四',20)
# print(p1.get_age())
#
# # 使用私有方法, 对内组装操作细节, 对外暴露简单的访问接口, 降低程序的复杂度
# class ATM:
#     def __card(self):
#         print('插入银行卡')
#     def __authorization(self):
#         print("输入密码认证用户")
#     def __view_balance(self):
#         print("查看余额")
#     def __get_money(self):
#         print("余额")
#     def withdraw(self):
#         self.__card()
#         self.__authorization()
#         self.__view_balance()
#         self.__get_money()
#
# wd = ATM()
# #直接调用公开的 withdraw() 方法, 实现内部复杂的操作
# wd.withdraw()

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def __str__(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 80:
#             return 'B'
#         elif self.score >= 70:
#             return 'C'
#         elif self.score >= 60:
#             return 'D'
#         else:
#             return 'E'
#
# s = Student("XiaoMing",88)
# print(s)
#
# class Human:
#     def __init__(self, name,height):
#         self.name = name
#         self.height = height
#     def __str__(self):
#         return f"名称：{self.name}，体重{self.height:.2f}"
#     def run(self):
#         self.height = self.height - 0.1
#     def eat(self):
#         self.height = self.height + 0.2
#
#
# x = Human("xiao",90)
# x.run()
# print(x)
# x.eat()
# x.eat()
# print(x)

class BankAccount:
    def __init__(self, account_name):
        self.account_name = account_name
        self.__balance = 0
    def __valid_amount(self, amount):
        if isinstance(amount, int):
            if 0 < amount <= 10000:
                return True
            print("金额不合法")
            return False
    def save_money(self,amount):
        if self.__valid_amount(amount):
            self.__balance += amount
            print(self)
        else:
            print("请重新输入正确的金额")

    def get_money(self,amount):
        if self.__valid_amount(amount):
            if self.__balance >= amount:
                self.__balance -= amount
                print(self)
            else:
                print("余额不足")

    def __str__(self):
        return f"用户名：{self.account_name}，余额：{self.__balance}"

bank = BankAccount("zhang_san")
bank.save_money(20000)
bank.save_money(3000)
bank.get_money(2500)