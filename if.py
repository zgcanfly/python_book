#coding=utf-8

#迭代器

list=[1,2,3,4]

it=iter(list)


#for i in it:
#    print(i,end=' ')


for i in range(len(list)):
    print(next(it))
