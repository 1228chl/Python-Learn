# 定义一个人类
class Person:
    def speak(self):
        print("我拥有说话的能力")
    def walk(self):
        print("我拥有走路的能力")
# 定义继承的老师类
class Teacher(Person):
    pass
# 定义学生类继承于人类
class Student(Person):
    pass

t = Teacher()
t.speak()
t.walk()
s = Student()
s.speak()
s.walk()

# 单继承(多层继承)
class Person(object):

    # 定义说话方法
    def speak(self):
        print(f"我拥有说话的能力")

    def walk(self):
        print(f"我拥有走路的能力")


# 定义学生类继承于人类
class Student(Person):
    pass


class CollegeStudent(Student):
    pass


# 创建大学生对象
college_stu = CollegeStudent()
college_stu.speak()
college_stu.walk()

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

#重写
class Car(object):
    def __init__(self):
        self.name = "汽车"
        self.wheel = 4
    def run(self):
        print(f"我拥有行驶的能力")
    def stop(self):
        print(f"我拥有停车的能力")
    def power(self):
        print(f"我拥有动力")
class OilCar(Car):
    """
        汽油车
    """
    def power(self):
        print(f"我拥有燃油动力")

class ElectricCar(Car):
    """
    电动车
    """
    def power(self):
        print(f"我拥有电池动力")

class HybridCar(OilCar, ElectricCar):
    """
    混动车
    """
    def __init__(self, battery):
        # super(HybridCar, self).__init__()
        super().__init__()
        self.battery = battery

    def power(self):
        # print(f"我拥有燃油和电池混合动力")
        OilCar.power(self)
        ElectricCar.power(self)
        print(f"我拥有燃油和电池混合动力")

# 创建混动车对象
hybrid_car = HybridCar("电池")
# 重写主要是实现子类个性化的功能, 重写父类同名的方法会覆盖继承的父类的方法
hybrid_car.power()
print(hybrid_car.battery)
print(hybrid_car.name)
print(hybrid_car.wheel)