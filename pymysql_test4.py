#coding=utf-8

import pymysql
db=pymysql.connect("192.168.1.74","root","password","yuangg")
cursor=db.cursor()
sql="select * from employee  where income > '%d'" %(1000)
try:
    cursor.execute(sql)
    #获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname =%s,age=%d,sex=%s,income=%d" %(fname,lname,age,sex,income))

except:
    print("Error : unable to fetch data")
db.close()

