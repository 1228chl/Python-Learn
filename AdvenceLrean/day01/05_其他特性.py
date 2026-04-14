class Car:
    wheel = 4
    count = 0

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        Car.count += 1
    def run(self):
        print(f"{self.brand}汽车开始行驶")
    def __str__(self):
        return f"{self.brand}汽车颜色是{self.color}，轮子{self.count}个"
c1 = Car("保时捷","黑色")
print(c1.count)
c1.wheel = 6 # 使用`对象.类属性`修改类属性，只会影响调用对象
print(c1.wheel)
Car.wheel = 8 # 使用`类名.类属性`修改类属性，会影响所有对象
c2 = Car("法拉利","黑色")
print(c2.count)
print(c2.wheel)


class Car:
    wheel = 4
    count = 0

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        Car.count += 1

    @classmethod
    def get_count(cls):
        print(f"创建的汽车数量是：{cls.count}")
    @classmethod
    def set_wheel(cls,wheel):
        cls.wheel = wheel
        print(cls.wheel)
    @classmethod
    def set_count(cls):
        cls.count = 0
        print("重新把汽车数量置为0，重新计数")

    def __str__(self):
        return f"{self.brand}汽车颜色是{self.color}，轮子{self.wheel}个"

c3 = Car("奔驰","白色")
c3.get_count()
c4 = Car("fala","black")
Car.get_count()
Car.set_count()
Car.get_count()
Car.set_wheel(8)
print(c3)

# 开发一款游戏
class Game(object):
    # 开始游戏，打印游戏功能菜单
    @staticmethod
    def menu():
        print('1、开始游戏')
        print('2、游戏暂停')
        print('3、退出游戏')
    @staticmethod
    def sum_students(class_count,student_number):
        return class_count * student_number

# 开始游戏、打印菜单
Game.menu()
print(Game.sum_students(2,100))