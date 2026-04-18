"""
self关键字: 当前对象本身, 不需要传递实参, 默认传递对象本身
作用: 在类的内部调用属性和方法


定义对象方法:  在类的内部定义
def 方法名(self[, 形参1, 形参2, ...]):
    pass

调用对象方法:
类外: 对象名.方法名([实参1, 实参2, ...])
类内: self.方法名([实参1, 实参2, ...])
"""


# todo:1-创建汽车类
class Car(object):
    # todo:2-定义跑的方法  方法和函数基本没有区别
    def run(self):
        print(f'self--->{self}')
        print('汽车正在飞速地运行...')

    # 定义方法, 调用run方法
    def call_run(self):
        print('在类内调用对象方法....')
        self.run()


print('Car--->', Car)
# todo:3-创建对象
# 对象1
su7 = Car()
print('su7--->', su7)
# 对象2
yu7 = Car()
print('yu7--->', yu7)
# todo:4-调用对象方法 类外
su7.run()
yu7.run()

print('=' * 80)
su7.call_run()
