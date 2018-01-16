#coding=utf-8

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
#plt.scatter表示散点图
plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")

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