#coding=utf-8

import plotly
import plotly.graph_objs

trace = plotly.graph_objs.Box(
    x=[1, 2, 3, 4, 5, 6, 7]
)
data = [trace]
plotly.offline.plot(data)  # 离线方式使用：offline