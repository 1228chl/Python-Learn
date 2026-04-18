"""
魔法方法: 以__开头, 以__结尾的对象方法, 并且在满足特定条件后会自动执行, 称为魔法方法
def __init__(self[, 形参1, 形参2, ...]): 构造方法, 初始化对象属性
def __str__(self):  print(对象名)会自动调用,  注意点: 必须要有返回值, 返回值类型必须是字符串类型
def __del__(self):  删除对象或程序允许结束后会自动调用, 内存回收(python中有自动的内存回收机制)
"""


class Car(object):
    def __init__(self, name, wheel, color):
        self.name = name
        self.wl = wheel
        self.color = color

    def __str__(self):
        return f'汽车名称是:{self.name}, 汽车轮胎数量是:{self.wl}, 汽车颜色是:{self.color}'

    def __del__(self):
        print('对象被删除了...')


su7 = Car('su7', 4, '霞光紫')
print(su7)
del su7