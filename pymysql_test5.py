#coding=utf-8
import pymysql

host =  '192.168.1.74'
user = 'root'
passwd = 'password'
dbase = 'yuangg'



db=pymysql.connect(host,user,passwd,dbase)
cursor = db.cursor()
sql = "select * from employee"

cursor.execute(sql)
results = cursor.fetchall()
for i in results:
    fname = i[0]
    lname = i[1]
    age = i[2]
    sex = i[3]
    income = i[4]
    print("fname=%s"%(fname))
db.close()