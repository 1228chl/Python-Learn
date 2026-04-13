# # topic-1
# # 设计一个类，可以记录 姓名、年龄、性别三种信息 （使用成员属性），
# # 并开发方法（方法名 show_info) 可以通过print打印记录的这些信息。
# class Man:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def show_info(self):
#         print(f"姓名{self.name}年龄{self.age}性别{self.sex}")
# m = Man("z",18,"man")
# m.show_info()

# # topic-2
# # 设计一个类，可以记录 姓名、年龄、性别三种信息 （使用成员属性）
# # 并开发方法（方法名 show_info) 可以通过print打印记录的这些信息。
# class Man:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __str__(self):
#         return f"姓名:{self.name}年龄:{self.age}性别:{self.sex}"
#     def show_info(self):
#         print(f"姓名{self.name}年龄{self.age}性别{self.sex}")
# m = Man("z",18,"man")
# m.show_info()

# # topic-3
# # 设计一个类，可以记录name和age 2个成员属性，
# # 要求使用`__init__`构造方法，在创建类对象的时候为name和age赋值。
# # 然后提供如下方法：
# # 1. get_name()  返回name字符串
# # 2. set_name(new_name)  修改name
# # 3. get_age() 返回age数字
# # 4. set_age(new_age) 修改age
# class Man:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_name(self,name):
#         self.name=name
#     def set_age(self,age):
#         self.age=age

# # topic-4
# # 设计一个 Student 类，包含私有成员 __name、__age、__score。
# # 使用 `__init__` 构造方法初始化这三个属性。
# # 提供 `get_name()`、`get_age()`、`get_score()` 方法获取私有属性。
# # 提供 `set_score(new_score)` 方法修改分数（分数必须是 0-100 的整数）。
# # 实现 `__del__` 方法，在对象被销毁时打印 `“学生[姓名]的信息已被销毁”`。
# class Student(object):
#     def __init__(self, name,age,score):
#         self.__name = name
#         self.__age = age
#         self.__score = score
#     def get_score(self):
#         return self.__score
#     def get_name(self):
#         return self.__name
#     def get_age(self):
#         return self.__age
#     def set_score(self,score):
#         if isinstance(score,int):
#             if 0 <= score <= 100:
#                 self.__score = score
#     def __del__(self):
#         print(f"学生{self.name}的信息已被销毁")
# s = Student("z",15,60)
# print(f"{s.name}..{s.age}..{s.get_score()}")
# del s

# # topic-5
# # 设计`Phone`类，要求：
# # 1. 用`__init__`初始化**私有属性**`__brand`（品牌）；
# # 2. 写`get_brand()`方法获取品牌、`set_brand()`方法修改品牌；
# # 3. 无复杂判断，传啥值就用啥值。
# class Phone:
#     def __init__(self,brand):
#         self.__brand = brand
#     def get_brand(self):
#         return self.__brand
#     def set_brand(self,brand):
#         self.__brand = brand
# p = Phone("dfsdf")
# print(p.get_brand())

# # topic-6
# # 设计`Dog`类，要求：
# # 1. 用`__init__`初始化公有属性`name`（名字）；
# # 2. 写`bark()`方法，调用时打印：`XXX：汪汪汪`（XXX 是狗的名字）。
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def bark(self):
#         print(f"{self.name}:Woof!")
# d = Dog("Bod")
# d.bark()

# # topic-7
# # 设计`Book`类，要求：
# # 1. 用`__init__`初始化**私有属性**`__title`（书名）；
# # 2. 写`get_title()`方法获取书名；
# # 3. 实现`__del__`方法，销毁时打印：`《XXX》书籍信息已清理`。
# class Book:
#     def __init__(self,title):
#         self.__title=title
#     def get_title(self):
#         return self.__title
#     def __del__(self):
#         print(f"{self.__title} has been deleted")
# b = Book("Python")
# del b

# # topic-8
# # ATM案例，实现一个类ATM，在内部提供
# # - 属性 balance（余额）
# # - 属性 password（密码）
# # - 方法 取钱，传入金额，余额减少
# # - 方法 存钱，传入金额，余额增加
# # - 方法 查看余额，输出余额
# # - 方法 验证密码，传入一个密码，验证是否正确
# # 要求，存取查看余额三个方法，在工作前都必须验证密码，`密码只需要输入一次`
#
# class ATM:
#     def __init__(self,balance,password):
#         self.balance=balance
#         self.password=password
#     def yanzheng(self):
#         password = input("请输入密码")
#         if password == self.password:
#             return True
#         return False
#     def quqian(self,amount):
#         if self.yanzheng():
#             self.balance -= amount
#     def cunqian(self,amount):
#         if self.yanzheng():
#             self.balance += amount
#     def chakan(self):
#         if self.yanzheng():
#             print(f"余额还有：{self.balance}")
# a = ATM(0,"1234")
# a.cunqian(3000)
# a.chakan()
# a.quqian(100)
# a.chakan()

# topic-9
# 思考优化上述案例8的优化点。
# - 私有password
# 可以有效的防止密码被篡改，提高安全性，最好将密码加密
# - 私有check_password 和 5次错误锁定 和密码格式校验和检查
# 检验密码可以有效防止恶意登录，5次错误锁定可以防止暴力破解，格式校验防止代码注入
# - 私有余额，  取钱大于余额判定
# 可以有效的防止数据出错和程序出错，对用户也是有好处的
# - 私有余额减少方法，内部做检验和日志记录
# 先密码怕段，判断余额是否足够，在进行余额的扣除，其中所有日志都要精确到秒
# - 私有余额增加方法，内部做检验和日志记录
# 同上
# - 抽象通用的 负数判定 字符串判定 整数判定 范围判定ATM最大支持一次2000操作
# 现实生活中防止大额诈骗，和用户乱数，和响应反馈的问题
# - 切换用户功能
# 拥有更好的用户体验

