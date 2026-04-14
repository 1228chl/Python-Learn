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
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod
    def show_help():
        print('-' * 40)
        print('【start】开始游戏')
        print('【stop】结束游戏')
        print('-' * 40)
    @classmethod
    def show_top_score(cls):
        print(f'本游戏的历史最高分：{Game.top_score}')
    def start_game(self):
        print(f'{self.player_name}开始游戏')
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
# Game.menu()
# print(Game.sum_students(2,100))
Game.show_help()
Game.show_top_score()

game = Game("itheima")
game.start_game()

class Payment:
    pay_rate = 0.05
    acount_balance = 0

    def __init__(self,balance=0):
        if balance > 0:
            self.balance = balance

    def pay(self,amount):
        if amount:
            print(f"pay {amount*(1 + self.pay_rate)}")
            self.acount_balance -= amount * (1 + self.pay_rate)

    @classmethod
    def set_pay_rate(cls,pay_rate):
        cls.pay_rate = pay_rate

    @staticmethod
    def cheak_amount(amount):
        if 0 < amount <= 5000:
            return amount
        else:
            print("金额超出范围")

    def __str__(self):
        return f"账户余额：{self.acount_balance}"

payment = Payment()
amount = payment.cheak_amount(1000)
payment.pay(amount)
print(payment.pay_rate)
Payment.set_pay_rate(0.08)
print(Payment.pay_rate)
payment.pay(amount)