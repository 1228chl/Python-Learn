# 定义一个人类
class Person:
    def speak(self):
        print("我拥有说话的能力")
    def walk(self):
        print("我拥有走路的能力")
class Student(Person):
    pass
class Teacher(Person):
    pass

t = Teacher()
t.speak()
t.walk()
s = Student()
s.speak()
s.walk()

class Car:
    def __init__(self):
        self.name = "汽车"
        self.wheel = 4
    def run(self):
        print("我拥有行驶的能力")
    def stop(self):
        print("我拥有停车的能力")

class OilCar(Car):
    def oil_power(selfs):
        print("我拥有燃油能力")

class EletricCar(Car):
    def electric_power(self):
        print("我拥有电池能力")

class HybridCar(OilCar,EletricCar):
    pass
hybrid_car = HybridCar()
hybrid_car.oil_power()
hybrid_car.electric_power()
hybrid_car.run()
hybrid_car.stop()
print(hybrid_car.name)
print(hybrid_car.wheel)
