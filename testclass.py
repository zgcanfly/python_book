#coding=utf-8

class parent:
    def myMethod(self):
        print("调用父类方法")

class child(parent):
    def myMethod(self):
        parent.myMethod(self)

s=child()
s.myMethod()