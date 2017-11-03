#encoding:utf-8
import math


a=4
b=3
last1=10
last2=20
yuangg="www.yuangg.com"
zgyang="yangzhiguang"
para_sar="""this is string
use string can task be table 
TAB ( \t )
or use [ \n ]
"""
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



list = [ 1 ,3,4,5,6,"a","b","c"]

if a in list:
    print("a in list")
elif b in list:
    print("b in list")
elif b not in list:
    print("b not in list")
elif a not in list:
    print("a not in list")
else:
    print("however , you are here ")

print("yuangg:",yuangg[0:])
print("zgyang:",zgyang)

print("zgyu:",zgyang[4:]+yuangg[4:6]*2)

print("My name is: %s and from: %s"%(zgyang,yuangg))

print(para_sar)
