#coding=utf-8

import pymysql
db=pymysql.connect("192.168.1.74","root","password","yuangg")

cursor=db.cursor()

sql="""insert into employee(first_name,last_name,age,sex,income)
        values ('mac', 'zgyang',20,'M',2000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()