#coding=utf-8

import plotly
from plotly.graph_objs  import *


trace0=Surface(
	colorscale='Viridis',
	z=[
		[3,5,8,13],
		[21,13,8,5]
	]
)
data=[trace0]
plotly.offline.plot(data)