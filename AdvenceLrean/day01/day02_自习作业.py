# 基础
import random


# topic-1
class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def study(self):
        print(f"{self.name} 在学习")
s = Student("zhangsan")
s.study()


# topic-2
class Bag:
    def __init__(self,color,size):
        self.__color=color
        self.__size=size

    def get_info(self):
        return f"颜色:{self.__color},尺寸:{self.__size}"
b = Bag("red","大")
print(b.get_info())


# topic-3
class Clock:
    def __init__(self, brand):
        self.brand = brand

    def ring(self):
        print(f"{self.brand}闹钟:叮铃铃")

    def __del__(self):
        print(f"{self.brand}闹钟已关闭")
c = Clock("A")
c.ring()
del c


# topic-4
class Animal:
    def speak(self):
        print("动物发出叫声")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")
a = Animal()
a.speak()
c = Cat()
c.speak()


# topic-5
class Cup:
    def __init__(self):
        self.__water = 0

    def add_water(self, water):
        self.__water += water

    def get_water(self):
        return self.__water
c = Cup()
c.add_water(10)
print(c.get_water())


# topic-6
class Teacher:
    def __init__(self,name):
        self.name = name

class MathTeacher(Teacher):
    def __init__(self, name, grade):
        super().__init__(name)
        self.__grade = grade

    def get_grade(self):
        return self.__grade
m = MathTeacher("A",60)
print(m.get_grade())


# 中等

# topic-1
class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def get_info(self):
        print(f"{self.__name}, {self.__age}, {self.__score}")

    def __str__(self):
        return f"学生：{self.__name}，年龄：{self.__age}，成绩：{self.__score}"
s = Student("A",15,22)
s.get_info()
print(s)


# topic-2
class Car:
    total_cars = 0

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        Car.total_cars += 1

    @classmethod
    def show_total(cls):
        print(cls.total_cars)
c = Car("name","red")
Car.show_total()


# topic-3
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def mul(a,b):
        return a * b

    @staticmethod
    def div(a,b):
        if b == 0:
            return "除数不能为0"
        return a / b
c = Calculator()
print(c.add(1, 2))
print(c.sub(3, 2))
print(c.mul(4, 3))
print(c.div(2, 0))
print(c.div(0, 2))


# topic-4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}吃东西")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name}正在学习,学号:{self.student_id}")

s = Student("张三",123,333)
s.eat()
s.study()


# topic-5
class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        if amount <= 0:
            return "存款金额不能为负数"
        self.__balance += amount
        return f"cun ru {amount}"

    def withdraw(self,amount):
        if amount > self.__balance:
            return "余额不足"
        self.__balance -= amount
        return f"qu chu {amount}"

    def get_balance(self):
        return self.__balance

b = BankAccount()
print(b.deposit(3000))
print(b.deposit(0))
print(b.withdraw(2000))
print(b.withdraw(2000))
print(b.get_balance())


# topic-6
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __str__(self):
        return f"《{self.title}》- 作者：{self.author}，价格：{self.price}元"
b = Book("A","B",11)
c = Book("C","D",21)
print(b < c)
print(b)
print(c)


# topic-7
class Employee:
    company = ["开发", "测试", "产品", "设计"]
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @staticmethod
    def is_valid_position(position):
        if position in Employee.company:
            return True
        return False

e = Employee("a","开发")
print(e.is_valid_position(e.position))


# topic-8
class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius**2

c = Circle(5)
print(c.get_area())
r = Rectangle(5,5)
print(r.get_area())


# topic-9
class Teacher:
    def __init__(self):
        self.__courses=list()

    def add_course(self,course):
        if course in self.__courses:
            print("课程已存在")
        self.__courses.append(course)

    def remove_course(self,course):
        if course not in self.__courses:
            print("课程不存在")
        self.__courses.remove(course)

    def show_courses(self):
        for course in self.__courses:
            print(course)
t = Teacher()
t.add_course("A")
t.add_course("A")
t.add_course("B")
t.remove_course("A")
t.remove_course("A")
t.show_courses()


# topic-10
class MobilePhone:
    system = "Android"

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    @classmethod
    def change_system(cls,system):
        MobilePhone.system = system

    def __str__(self):
        return f"品牌：{self.brand}，型号：{self.model}，系统：{self.system}"
m = MobilePhone("XioaMi","A001")
print(m)
MobilePhone.change_system("Apple")
print(m)


# topic-11
class Movie:
    def __init__(self,name,duration):
        self.name=name
        self.duration=duration

    def __add__(self, other):
        return self.duration+other.duration

    def __str__(self):
        return f"电影：{self.name}，时长：{self.duration}分钟"
m = Movie("A",120)
print(m)
o = Movie("B",120)
print(o)
print(m+o)


# topic-12
class Pet:
    def speak(self):
        pass

class Dog(Pet):
    def speak(self):
        print("wang")

class Cat(Pet):
    def speak(self):
        print("miao")

def make_speak(pet):
    print(pet.speak())
dog = Dog()
cat = Cat()
make_speak(dog)
make_speak(cat)


# topic-13
class Product:
    def __init__(self):
        self.__price = 10

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price <= 0:
            print("价格不能为负数或0")
            return
        self.__price = price

p = Product()
print(p.get_price())
p.set_price(20)
print(p.get_price())
p.set_price(0)


# topic-14
class Team:
    member_count = 0
    def __init__(self):
        self.members = list()

    def add_member(self, member):
        self.members.append(member)
        type(self).member_count += 1

    def remove_member(self, member):
        self.members.remove(member)
        type(self).member_count -= 1

    @classmethod
    def show_total(cls):
        return Team.member_count
t = Team()
t.add_member("a")
t.add_member("b")
t.remove_member("b")
t.add_member("c")
t.add_member("d")
print(t.show_total())


# topic-15
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"向量(X:{self.x}, Y:{self.y})"
v = Vector(2, 3)
print(v)
x = Vector(4,5)
print(v*x)


# topic-16
class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def run(self):
        pass

class Rabbit(Animal):
    def __init__(self, color, name, age):
        super().__init__(name, age)
        self.color = color

    def run(self):
        print(f"{self.name}（{self.color}）正在蹦蹦跳跳")

class Horse(Animal):
    def __init__(self, name, age,speed):
        super().__init__(name, age)
        self.speed = speed

    def run(self):
        print(f"{self.name} 正在以{self.speed}km/h的速度奔跑")

r = Rabbit("A",12,"red")
r.run()
h = Horse("B",14,123)
h.run()


# topic-17
class ShoppingCart:
    def __init__(self):
        self.__items = list()

    def add_item(self, name, count, price):
        for item in self.__items:
            if item[0] == name:
                item[1] += count
        self.__items.append([name, count, price])

    def remove_item(self, name):
        for item in self.__items:
            if item[0] == name:
                self.__items.remove(item)
                return "商品已删除"
        else:
            print("商品不存在")

    def get_total(self):
        ans = 0
        for i in self.__items:
            ans += i[2]
        return ans
s = ShoppingCart()
s.add_item("A",3,55)
s.add_item("B",2,99)
s.add_item("A",1,55)
print(s.remove_item("A"))
print(s.get_total())


# topic-18
class Game:
    player_count = 0

    def __init__(self, name):
        if self.is_valid_username(name):
            self.name = name
            Game.player_count += 1

    @staticmethod
    def is_valid_username(name):
        if 3 <= len(name) <= 10 and name.isalnum():
            return True
        return False
g = Game("ada.")
g1 = Game("ada22")
print(Game.player_count)


# topic-19
class Person:
    def __init__(self, id_card):
        self.__id_card = id_card

    def get_id_card(self):
        temp = str(self.__id_card)
        return temp[0:6]+"********"+temp[-4:]

p = Person("123456789012345678")
print(p.get_id_card())


# topic-20:
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() == other.get_area()

    def get_area(self):
        return self.width * self.height

r1 = Rectangle(6,5)
r2 = Rectangle(5,5)
print(r1 == r2)


# 困难
# topic-1
class Base:
    def __init__(self,code,**kwargs):
        self.code = code
        print(f"Base初始化：code={code}")

class A(Base):
    def __init__(self,code,name,**kwargs):
        super().__init__(code=code,name=name ,**kwargs)
        self.name = name
        print(f"A初始化：name={name}")

class B(Base):
    def __init__(self,code,name,**kwargs):
        super().__init__(code=code,name=name,**kwargs)
        self.name = name
        print(f"B初始化：name={name}")

class C(A,B):
    def __init__(self,code,name,num,**kwargs):
        super().__init__(code=code,name=name,**kwargs)
        self.num = num
        print(f"C初始化：num={num}")

    def __str__(self):
        return f"C(code:{self.code}, name:{self.name}, num:{self.num})"

c = C(code=1001,name="test",num=99)
print(c)


# topic-2
class Commodity:
    def __init__(self,sku,name,price,stock):
        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__cost_price = price
        self.__stock = stock
        self.__sales = 0

    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("新价格必须大于0")
        if new_price < self.__cost_price:
            raise ValueError(f"新价格不能低于成本价({self.__cost_price})")
        old_price = self.__price
        self.__price = new_price
        self.show_price_log(old_price, new_price)

    def stock_in(self,num):
        if num > 0:
            self.__stock += num

    def stock_out(self,num):
        if num <= 0:
            raise ValueError("出库数量必须为正数")
        if num > self.__stock:
            raise ValueError(f"出库数量({num})超过当前库存({self.__stock})")
        self.__stock -= num
        self.__sales += num

    def get_commodity_info(self):
        return f"SKU:{self.__sku},名称:{self.__name},价格:{self.__price},库存:{self.__stock},销量:{self.__sales}"

    def show_price_log(self,old_price,new_price):
        print(f'old_price:{self.__price},new_price:{new_price}')
c = Commodity("AAAAAA01","A",12,100)
try:
    c.update_price(10)
except ValueError as e:
    print("价格更新失败:", e)
c.update_price(13)
c.stock_in(200)
c.stock_out(20)
try:
    c.stock_out(500)
except ValueError as e:
    print("出库失败:", e)
print(c.get_commodity_info())


# topic-3
class FileReader:
    li = list()

    def load(self, file_path):
        if not FileReader.li:
            with open(file_path, 'r', encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.rstrip('\n')
                    h = {}
                    li = list(line.split(","))
                    h['name']=li[0]
                    h['age']=li[1]
                    h['gender']=li[2]
                    FileReader.li.append(h)
        else:
            return FileReader.li.append(FileReader.li[0])
f = FileReader()
f.load("data.csv")
print(f.li)
f.load("data.csv")
print(f.li)


# topic-4
def A():
    a = 0
    def B():
        nonlocal a
        a += 1
        print(a)
    B()
    return B

a = A()
a()


# topic-5
class GuessNumberGame:
    def __init__(self):
        self.__num = random.randint(1, 100)
        self.count = 0
        self.is_over = True

    def reset(self):
        self.__num = random.randint(1, 100)
        self.count = 0
        print("\n" + "=" * 40)
        print("游戏已重置！新的目标数字已生成（1-100之间）")
        print("=" * 40 + "\n")

    def start_game(self):
        print("开始游戏")
        while self.is_over:
            n = int(input("请输入你要猜的数字"))
            self.count += 1
            if n == self.__num:
                print(f"恭喜你猜对了,总共猜了{self.count}次")
                choice = input("是否选择重玩Y/N").strip().upper()
                if choice == "Y":
                    self.reset()
                else:
                    self.is_over = False
            elif n > self.__num:
                print("猜大了")
            else:
                print("猜小了")
g = GuessNumberGame()
g.start_game()


# topic-6
class Vehicle:
    def horn(self):
        print("交通工具鸣笛")

class Car(Vehicle):
    def horn(self):
        print("嘀嘀嘀")

class Train(Vehicle):
    def horn(self):
        print("呜呜呜")

class Bike(Vehicle):
    pass
def make_horn(v):
    v.horn()
v = Vehicle()
c = Car()
t = Train()
b = Bike()
make_horn(v)
make_horn(c)
make_horn(t)
make_horn(b)


# topic-7
class Fruit:
    def introduce(self):
        print("这是一种水果")

class FleshFruit(Fruit):
    def introduce(self):
        print("这是果肉果，果肉饱满")

class Apple(FleshFruit):
    def introduce(self):
        print("这是苹果，酸甜可口")

class Banana(FleshFruit):
    def introduce(self):
        print("这是香蕉，软糯香甜")

class Cherry(Fruit):
    pass

def show_fruit(fruit):
    fruit.introduce()

fruit = Fruit()
ffruit = FleshFruit()
apple = Apple()
banama = Banana()
cherry = Cherry()
show_fruit(fruit)
show_fruit(ffruit)
show_fruit(apple)
show_fruit(banama)
show_fruit(cherry)


# topic-8
class ScoreManager:
    def __init__(self):
        self.__score = 0
        self.__check_code = '8888'
        self.__error_count = 0

    def verify_code(self,code):
        if self.__error_count <= 3:
            if code == self.__check_code:
                return True
            else:
                self.__error_count += 1
                return False
        else:
            return False

    def set_score(self,score):
        if self.__check_score(score):
            self.__score = score
        else:
            print('请输入合法范围成绩0-100')

    def update_score(self,score):
        x = self.__score + score
        if 0 <= x <= 100:
            self.__score = x
        else:
            print("输入的成绩之和不能小于0或大于100")

    def get_score(self):
        return f'分数为：{self.__score}'

    def __check_score(self,num):
        if not isinstance(num, int):
            print(f"错误：成绩必须是整数，你输入的是{type(num)}")
            return False
        if num < 0 or num > 100:
            print("错误：成绩必须在0-100之间")
            return False
        return True

if __name__ == '__main__':
    sm = ScoreManager()
    flag = False
    for i in range(3):
        code = input("请输入操作验证码")
        if sm.verify_code(code):
            flag = True
            break

    while flag:
        try:
            opt = int(input("\n请选择操作（1-查询 2-设置成绩 3-修改成绩 其他-退出）："))
            if opt == 1:
                print(sm.get_score())
            elif opt == 2:
                score = int(input("请输入要设置的成绩(0-100):"))
                sm.set_score(score)
            elif opt == 3:
                num = int(input("请输入成绩修改值（正数加/负数减）："))
                sm.update_score(num)
            else:
                print("退出系统")
                break
        except ValueError:
            print("输入错误，请输入数字选项")


# topic-9
class ShoppingCart:
    def __init__(self):
        self.__cart = {}
        self.__pwd = "1234"
        self.__err_times = 0

    def check_pwd(self, pwd):
        if pwd == self.__pwd:
            return True
        return False

    def add_goods(self,name,num):
        if name in self.__cart and self.__check_num(num):
            self.__cart[name] += num
        else:
            self.__cart[name] = num

    def del_goods(self, name,num):
        if name in self.__cart:
            if self.__check_num(num) and self.__cart[name] >= num:
                self.__cart[name]-=num

    def settle(self):
        items = [(name,num) for name,num in self.__cart.items()]
        total_num = sum(self.__cart.values())
        return items,total_num

    def __check_num(self,num):
        if not isinstance(num,int) or num < 0:
            return False
        else:
            return True

if __name__ == '__main__':
    s = ShoppingCart()
    flag = False
    for i in range(5):
        code = input("请输入操作验证码")
        if s.check_pwd(code):
            flag = True
            break
    while flag:
        try:
            opt = int(input("\n请选择操作（1-添加商品 2-删除商品 3-结算购物车 其他-退出）："))
            if opt == 1:
                name = input("请输入商品名称")
                num = int(input("请输入商品数量"))
                print(s.add_goods(name,num))
            elif opt == 2:
                name = input("请输入商品名称")
                num = int(input("请输入商品数量"))
                s.del_goods(name,num)
            elif opt == 3:
                print(s.settle())
            else:
                print("退出系统")
                break
        except ValueError:
            print("输入错误，请输入数字选项")


# topic-10
class BookManager:
    def __init__(self):
        self.__books = {"python":10,"java基础":8,"c":5}
        self.__key = "admin666"
        self.__key_err = 0

    def verify_key(self, key):
        if self.__key_err <= 4:
            if key == self.__key:
                return True
            else:
                self.__key_err += 1
                return False
        else:
            return False

    def borrow_book(self,name,num):
        if self.__check_borrow_num(name,num):
            self.__books[name] -= num

    def return_book(self,name,num):
        if self.__check_return_num(num):
            if name in self.__books:
                self.__books[name] += num
            else:
                self.__books[name] = num

    def query_book(self,name):
        if name == "":
            item = [(key,value) for key,value in self.__books.items()]
        else:
            item = [name,self.__books[name]]
        return item

    def __check_borrow_num(self,name,num):
        if name in self.__books:
            if isinstance(num,int):
                if self.__books[name] >= num:
                    return True
                else:
                    print("借阅数量过多，图书不够")
                    return False
            else:
                print("请输入整数")
                return False
        print("图书不存在")
        return False

    def __check_return_num(self,num):
        if isinstance(num,int):
            return True
        print("请输入正整数")
        return False

if __name__ == '__main__':
    b = BookManager()
    flag = False
    for i in range(5):
        code = input("请输入操作验证码")
        if b.verify_key(code):
            flag = True
            break
    while flag:
        try:
            opt = int(input("\n请选择操作（1-借阅图书 2-归还图书 3-查询图书 其他-退出）："))
            if opt == 1:
                name = input("请输入图书名称")
                num = int(input("请输入图书数量"))
                b.borrow_book(name,num)
            elif opt == 2:
                name = input("请输入图书名称")
                num = int(input("请输入图书数量"))
                b.return_book(name,num)
            elif opt == 3:
                name = input("请输入图书名称（不输入则查询全部）")
                print(b.query_book(name))
            else:
                print("退出系统")
                break
        except ValueError:
            print("输入错误，请输入数字选项")