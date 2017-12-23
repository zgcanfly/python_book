#coding=utf-8
import pandas as pd
import pymysql
db=pymysql.connect("192.168.1.74","root","password","chinesestock",charset='utf8')
cursor=db.cursor()
sql="select * from daily_price where price_date > '2017-10-01'"
list_id = []
list_stock_id = []
list_code = []
list_price_date = []
list_open = []
list_close = []
list_high = []
list_low = []
list_volume= []



cursor.execute(sql)
#获取所有记录列表
results = cursor.fetchall()
for row in results:
    id = row[0]
    stock_id = row[1]
    code = row[2]
    price_date = row[3]
    open = row[4]
    close = row[5]
    high = row[6]
    low = row[7]
    volume = row[8]
    list_id.append(id)
    list_stock_id.append(stock_id)
    list_code.append(code)
    list_price_date.append(price_date)
    list_open.append(open)
    list_close.append(close)
    list_high.append(high)
    list_low.append(low)
    list_volume.append(volume)
df = pd.DataFrame({'id':list_id,
                   'stock_id':list_stock_id,
                   'code':list_code,
                   'date':list_price_date,
                   'open':list_open,
                   'close':list_close,
                   'high':list_high,
                   'low':list_low,
                   'volume':list_volume})
print(df)
db.close()