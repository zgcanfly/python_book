#coding=utf-8

dict={'alice':'1','beth':'2','zgyang':'3'}
dict3={'alice':'a','yuangg':'k','beijing':'12'}

print(dict)

print(dict['alice'],dict['beth'])

dict['yuangg']='4'
print(dict['yuangg'])

dict['yuangg']='6'
print(dict)

print("--------------------\n")
print("字典以字符串的方式列出")
print(str(dict))
print("字典的个数")

print(len(dict))

if "yuangg" in dict:
    print("yuangg in dict\n")
else:
    print("yuangg not in dict")

print(dict.items())
print("以下是字典中所有的key值\n")
print(dict.keys())

print("--------------------\n")
print("删除 dict")
del dict['yuangg']

print(dict)
dict.clear()
print(dict)
del dict
print(dict)
