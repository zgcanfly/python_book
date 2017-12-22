#coding=utf-8

import pymysql
db=pymysql.connect("192.168.1.74","root","password","chinesestock",charset='utf8')
cursor=db.cursor()
sql="select * from daily_price where price_date >'2017-11-01' "

cursor.execute(sql)
#获取所有记录列表
results = cursor.fetchall()
print(results)
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    print(fname,lname,age,sex,income)

db.close()

