class Animal:
    def speak(self):
        print("说话的能力")
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def animal_speak(obj):
    obj.speak()

animal = Animal()
dog = Dog()
cat = Cat()
animal_speak(animal)
animal_speak(dog)
animal_speak(cat)

class Alipay:
    def pay(self, amount):
        print(f'支付宝支付了{amount}元')

class WechatPay:
    def pay(self, amount):
        print(f"微信支付了{amount}元")

class CreditPay:
    def pay(self, amount):
        print(f"信用卡支付了{amount}元")

def payment(obj):
    obj.pay(100)

alipay = Alipay()
wechatpay = WechatPay()
creditpay = CreditPay()
payment(alipay)
payment(wechatpay)
payment(creditpay)
