#encode:utf-8

list1=['google','robot','yuangg',1995]
list2=[1,2,6,4,5]
list3=["a","b","c","d"]

print(list1)
print(list2)
print(list3)

list4=list1+list2+list3
print("list1+list2+list3=:",list4)
print(list4[2])
del list4[2]
print(list4)
list5=[list1,list2,list3,list4]
print(list5)
print(len(list5))
print(max(list2))
print(min(list2))
list4.append("zgyang")
print(list4)
print(list4.count("zgyang"))

for i in list5:
    list4.pop()
    print(list4)

list3.insert(0,"zgyang")
print(list3)
print(list3.index("zgyang"))
print(list3.remove("zgyang"))
print(list3)
list3.reverse()
print(list3)
list2.sort()
print(list2)
print(list1)
list1.clear()
print(list1)