"""
属性: 特征 变量 数据

定义属性:
类内:
借助 __init__ 魔法方法, 通过 self.属性名 = 属性值
类外:
对象名.属性名 = 属性值

调用属性:
类内: self.属性名
类外: 对象名.属性名
"""

# todo:1-创建汽车类
class Car(object):
    # todo:2-定义init魔法方法(构造方法), 初始化对象属性
    # 实例化对象/创建对象时会自动被调用
    def __init__(self, name, wheel):
        """
        :param name: 名称
        :param wheel: 轮胎数量
        """
        self.name = name
        self.wheel = wheel

    # todo:3-定义run方法, 调用对象属性
    def run(self):
        print(f"汽车名称: {self.name}, 汽车轮胎数量:{self.wheel}")


# todo:4-创建对象
su7 = Car('舒淇111', 4)
su7.run()

# 对象2
yu7 = Car('YU7', 5)
# todo:5-外部定义对象属性
yu7.color = '白色'
# todo:6-外部调用对象属性
print('yu7.name--->', yu7.name)
print('yu7.color--->', yu7.color)

Car('帕拉梅拉', 4).run()
print(Car('大G', 5).name)