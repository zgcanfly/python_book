#coding=utf-8

import pymysql

host =  '192.168.1.74'
user = 'root'
passwd = 'password'
dbase = 'yuangg'

db=pymysql.connect(host,user,passwd,dbase)

cursor=db.cursor()
sql="update employee set age = age +1 where sex = '%c' " %('F')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
