#coding=utf-8
class people:
    name=''
    age=0
    _weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print("%s 说: 我%d岁."%(self.name,self.age))

#单类继承
class student(people):
    grade=''
    def __init__(self,n,a,w,g):
    #调用父类的方法
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("%s说：我%d岁,在读%d年纪"%(self.name,self.age,self.grade))
y=people('ken',30,30)
s=student('tom',20,20,20)
s.speak()