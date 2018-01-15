import plotly.offline as py
import plotly.graph_objs as go

from datetime import datetime
import pandas_datareader.data as web

df = web.DataReader("aapl", 'yahoo',
                    datetime(2015, 1, 1),
                    datetime(2016, 7, 1))
#展示的是折线图
data = [go.Scatter(x=df.index, y=df.High)]
data1 = [go.Scatter(x=df.index, y=df.Low)]
#
print(df)
fig=[data,data1]
py.plot(fig)

