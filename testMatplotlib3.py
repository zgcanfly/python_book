#coding=utf-8

import matplotlib.pyplot as plt


population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
#plt.hist表示直方图
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
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