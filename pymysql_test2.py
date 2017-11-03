#coding=utf-8

import pymysql

db = pymysql.connect("192.168.1.74","root","password","yuangg")
cursor = db.cursor()
cursor.execute("drop table if exists employee")
sql="""create table employee(first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float )"""
cursor.execute(sql)
db.close()