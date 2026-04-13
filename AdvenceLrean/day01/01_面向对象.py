# defined class
class Person(object):
    # defined property
    name = "zhangsan"
    age = 18
    # defined method
    def speak(self):
        print(f"hello {self.name}")
    def eat(self):
        print(f"{self.name} eat")

p = Person()
p.speak()
p.eat()
print(p.name)
print(type(p.name))