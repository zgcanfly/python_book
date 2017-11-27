#coding=utf-8

import sys
def fibonacci(n,w=0):
    a,b,counter =0,1,0
    for i in range(n):
        yield a
        a,b=b,a+b
        print('%d,%d'%(a,b))
        counter +=1

f=fibonacci(10,0)

while True:
    try:
        print(next(f),end=" ")
    except:
        sys.exit()