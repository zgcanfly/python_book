#encoding:utf-8


a=10
b=20

def _init_(self, last1,last2):
    last3=last1+last2
    print("last1+last2=",last3)
    last3=last1*last2
    print("last1xlast2=",last3)
    last3=last1/last2
    print("last1/last2=",last3)

    if last2 != last1:
        print("last2!=last1")
    if last1 < last2:
        print("last1 < last2")
    if last1 > last2:
        print("last1 > last2")

