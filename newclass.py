#coding=utf-8

class Myclass:
    i=12345
    def f(self):
        return 'hello'

x=Myclass()

print("MyClass 类的属性i为：",x.i)
print("MyClass 类的方法f为：",x.f())

class Comlex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
y=Comlex(3.0,4.5)

print(y.r,y.i)

class people:
    #定义基本属性
    name=''
    age=0
    #私有方法无法在类的外部访问
    _weight=0
    #定义方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w

    def speak(self):
        print("%s 说 ：我 %d 岁"%(self.name,self.age))

p=people('tom',22,30)
p.speak()
