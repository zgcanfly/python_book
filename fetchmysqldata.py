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
print(results)
db.close()