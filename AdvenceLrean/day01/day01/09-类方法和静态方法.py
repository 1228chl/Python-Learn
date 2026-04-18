"""
对象(实例)方法:

类方法:
定义:
@classmethod
def 方法名(cls[, 形参1, 形参2, ...]):
    pass
调用: 类名.方法名()  或  对象名.方法名()
应用场景: 在类的内部访问类属性时

静态方法:
定义:
@staticmethod
def 方法名(形参1, 形参2, ...):
    pass
调用: 类名.方法名()  或  对象名.方法名()
应用场景: 方法中不需要通过self或cls调用属性时
"""


# 创建学生类
class Student():
    # 定义类属性  班级
    class_no = 'AI6期'

    # 定义init方法  -> 对象方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义获取类属性的类方法
    @classmethod
    def get_class_no(cls):
        print(Student.class_no)
        print(f"班级是: {cls.class_no}")

    # 定义静态方法, 输出普通信息
    @staticmethod
    def print_info():
        print('学生会学习')
        print('学生也会打游戏')


# 创建对象
s1 = Student('特朗普', 78)
# 调用对象方法
s1.__init__('川建国', 74)
print(s1.name)
print(s1.age)

print('=' * 80)
# 调用类方法
Student.get_class_no()
s1.get_class_no()

print('=' * 80)
Student.print_info()
s1.print_info()
