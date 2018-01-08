#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
x,y=np.loadtxt('examlp.txt',delimiter=',',unpack=True)
#折线图
plt.plot(x,y,label='Load from file')
#x
plt.xlabel('x')
#y
plt.ylabel('y')
#标题
plt.title('Interesting Graph\nCheck it out')
#图标
plt.legend()
#展示
plt.show()