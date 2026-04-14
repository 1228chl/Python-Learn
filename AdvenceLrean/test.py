class Car(object):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)
        self.kwargs = kwargs

class XiaoMi(Car):
    def __init__(self,color, **kwargs):
        super().__init__(**kwargs)
        self.color = color

    def run(self):
        print(f'{self.name} 汽车会漂移...')

class BenChi(Car):
    def __init__(self,price,**kwargs):
        super().__init__(**kwargs)
        self.price = price

    def run(self):
        print(f'{self.name} 汽车会狂飙...')


class XinGaiNai(XiaoMi,BenChi):
    def __init__(self,name,color,price,owner):
        super().__init__(name=name,color=color,price=price,owner=owner)

    def run(self):
        XiaoMi.run(self)
        BenChi.run(self)
        print(f'{self.name} 汽车会飞行...')

print(XinGaiNai.mro())

xiaomi = XiaoMi(name='小米',color='红色')
xiaomi.run()

benchi = BenChi(name='奔驰',price=34464746)
benchi.run()

xin_gai_nai = XinGaiNai('新概念', '钛金属', '89900','user')
xin_gai_nai.run()