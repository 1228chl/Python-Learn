"""
私有: 自己拥有的内容, 加访问权限
子类不能继承父类的私有属性或私有方法
私有属性或方法定义: 在类的内部定义 ->  __属性名  def __方法名(self):
调用: 只能在类的内部调用  self.__属性名   self.__方法名()
"""


# todo:1-创建汽车类
class Car():
    # todo:2-定义init魔法方法, 初始化属性
    def __init__(self, name, wheel, color):
        self.name = name  # 公有属性
        self.wheel = wheel
        self.__color = color  # 私有属性

    # todo:3-定义run私有方法
    def __run(self):
        print(f'汽车名称:{self.name}, 汽车颜色:{self.__color}, 汽车轮胎数量:{self.wheel}')

    # todo:4-定义公有方法, 调用私有方法
    def call_run(self):
        print(self.__color)
        self.__run()


# todo:5-创建子类
class WenJie(Car):
    pass


# todo:创建对象
su7 = Car('SU7', 4, '霞光紫')
# print(su7.__color)  # 报错, 不能在外部访问
# su7.__run()  # 报错, 不能在外部访问
su7.call_run()

# 创建对象
M7 = WenJie('M7', 4, '白色')
M7.call_run()
