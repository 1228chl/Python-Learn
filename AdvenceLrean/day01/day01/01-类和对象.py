"""
类: 一类具有相似特征和行为的事物统称, 泛指, 看不见摸不着

类定义:
class 类名(object):
    pass

类名: 标识符, 一般使用大驼峰命名

对象: 具有特征(属性)和行为(方法)的事物, 具体指向, 看得见摸得着
创建对象: 对象名 = 类名()
"""


# todo:1-创建汽车类
class Car(object):
    # todo:2-定义跑的方法  方法和函数基本没有区别
    def run(self):
        print('汽车正在飞速地运行...')


print('Car--->', Car)
# todo:3-创建对象
# 对象1
su7 = Car()
print('su7--->', su7)
# 对象2
yu7 = Car()
print('yu7--->', yu7)