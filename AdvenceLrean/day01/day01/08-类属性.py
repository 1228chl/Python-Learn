"""
类属性: 类拥有的属性
定义: 在类的内部方法之外  通过  属性名=属性值
调用: 类名.属性名  对象名.属性名  cls.属性名
注意点: 修改类属性 只能通过  类名.属性名=新值

好处: 所有对象的类属性都指向一份数据(共享数据), 节省内存空间
"""


# todo:1-创建类
class Student(object):
    # todo:2-定义类属性
    class_no = 'AI6期'

    # todo:3-定义init方法, 初始化对象属性
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建对象
s1 = Student('川建国', 74)
print(s1.name)
print(s1.age)
# 获取类属性
print(Student.class_no)
print(s1.class_no)
print('=' * 80)

s2 = Student('隔壁老王', 50)
print(Student.class_no)
print(s2.class_no)

print('=' * 80)
# 修改类属性
Student.class_no = 'AI7期'
print(Student.class_no)
print(s1.class_no)
print(s2.class_no)

# s1.class_no = 'AI7期'  # 给对象添加了一个新的属性, 和类属性重名而已
# print(s1.class_no)
