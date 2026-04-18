"""
多态: 不同类的同一个方法有不同的展现形式
条件: 1.继承  2.重写  3.父类引用指向子类对象(声明对象类型为父类)
python中的多态是伪多态, 可以没有1和3的条件
"""
from abc import ABC, abstractmethod


# todo:1-创建动物类
# 抽象类  规定了接口的标准, 不允许创建类对象
class Animal(ABC):
    # 定义叫方法  抽象方法
    @abstractmethod
    def speak(self):
        pass


# todo:2-创建狗类, 继承动物类
class Dog(Animal):
    # 重写叫方法
    def speak(self):
        print('汪汪汪')


# todo:3-创建猫类, 继承动物类
class Cat(Animal):
    # 重写叫方法
    def speak(self):
        print('喵喵喵')


# todo:4-定义公共接口  可以是函数 也可以是 类的方法
def animal_speak(obj: Animal):
    obj.speak()


# 创建对象
dog = Dog()
cat = Cat()

animal_speak(dog)
animal_speak(cat)

objs = [dog, cat]
for obj in objs:
    animal_speak(obj)

print('=' * 80)


# python中的伪多态, 可以没有继承和父类引用指向子类对象条件
# todo:1-创建动物类
class Animal:
    # 定义叫方法  抽象方法
    def speak(self):
        print('动物叫...')


# todo:2-创建狗类, 继承动物类
class Dog:
    # 重写叫方法
    def speak(self):
        print('汪汪汪')


# todo:3-创建猫类, 继承动物类
class Cat:
    # 重写叫方法
    def speak(self):
        print('喵喵喵')


# todo:4-定义公共接口  可以是函数 也可以是 类的方法
def animal_speak(obj):
    obj.speak()


# 创建对象
dog = Dog()
cat = Cat()

animal_speak(dog)
animal_speak(cat)