#coding=utf-8

import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)
#plt.stackplot表示堆叠图
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])


#x轴name
plt.xlabel('x')
#y轴name
plt.ylabel('y')
#标题
plt.title('Interesting Graph\nCheck it out')
#图标
plt.legend()
#展示
plt.show()