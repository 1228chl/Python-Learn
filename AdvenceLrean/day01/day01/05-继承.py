"""
继承: 子承父业, 子类继承父类的公有属性和方法
作用: 提高编程效率

继承语法:
class 子类(父类):
    pass

分类:
单继承: 一个子类只能有一个父类
多继承: 一个子类可以有多个父类
多层继承: 继承顺序链   A->B->C->D

重写操作: 在子类中定义和父类同名的属性或方法   ->   父类的属性或方法不能满足需求

在子类调用父类属性或方法:
super().方法名(): 适用于单继承
父类名.方法名(self): 适用于多继承
"""


# todo:1-创建父类1
class Master(object):
    def __init__(self):
        self.kongfu = '师傅制作煎饼果子的配方'

    def make_cake(self):
        print(f'师傅制作煎饼果子')

    def make_master_cake(self):
        print('师傅制作煎饼果子')


# todo:2-创建父类2
class School(object):
    def __init__(self):
        self.kongfu = '学校制作煎饼果子的配方'

    def make_cake(self):
        print('学校制作煎饼果子')

    def make_school_cake(self):
        print('学校制作煎饼果子')





# todo:3-创建子类
# 单继承
# class Prentice(Master):
#     pass

# 多继承
class Prentice(School, Master):  # 同名方法或属性, 从左到右就近原则继承
    def __init__(self):
        self.kongfu = '独创的制作煎饼子的配方'

    # 重写, 定义和父类同名的方法
    def make_cake(self):
        print('独创的制作煎饼果子')

    # 在子类中调用和父类同名的方法
    def call_school_cake(self):
        super().make_cake()
        School.make_cake(self)

    def call_master_cake(self):
        super().make_cake()
        Master.make_cake(self)


# 创建子类对象
p = Prentice()
print('p.kongfu--->', p.kongfu)
p.make_cake()
print('=' * 80)
p.make_school_cake()
p.make_master_cake()
print('=' * 80)
p.call_school_cake()
print('=' * 80)
p.call_master_cake()

print(Prentice.__mro__)
print(Prentice.mro())
