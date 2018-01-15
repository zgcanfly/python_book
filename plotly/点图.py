#coding=utf-8

import plotly
from plotly.graph_objs  import *

def line_plots():
  '''
  绘制普通线图
  '''
  #数据，x为横坐标，y,z为纵坐标的两项指标，三个array长度相同
  dataset = {'x':[0,1,2,3,4,5,6,7,8,9],
        'y':[5,4,1,3,11,2,6,7,19,20],
        'z':[12,9,0,0,3,25,8,17,22,5]}
  data_g = []
  #分别插入 y, z
  tr_x = Scatter(
    x = dataset['x'],
    y = dataset['y'],
    name = 'y'
  )
  data_g.append(tr_x)
  tr_z = Scatter(
    x = dataset['x'],
    y = dataset['z'],
    name = 'z'
  )
  data_g.append(tr_z)
  #设置layout,指定图表title,x轴和y轴名称
  layout = Layout(title="line plots", xaxis={'title':'x'}, yaxis={'title':'value'})
  #将layout设置到图表
  fig = Figure(data=data_g, layout=layout)
  #绘图,输出路径为name参数指定
  plotly.offline.plot(fig, filename='折线图.html')

if __name__=='__main__':
	line_plots()