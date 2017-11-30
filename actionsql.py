#coding=utf-8

import pymysql
host =  '192.168.1.74'
user = 'root'
passwd = 'password'
dbase = 'yuangg'
db=pymysql.connect(host,user,passwd,dbase)

cursor=db.cursor()

sql="delete from employee  where age > '%d'" % (20)
createdatasql="create database yuangg if not exists yuangg"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()