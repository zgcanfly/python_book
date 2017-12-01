#coding=utf-8
import random
li=[]
for i in range(10):
    r = random.randrange(0,5)
    if r ==2 or r ==4 :
        num = random.randrange(0,9)
        li.append(str(num))
    else:
        temp=random.randrange(65,91)
        c=chr(temp)
        li.append(c)

result=''.join(li)
print(result)