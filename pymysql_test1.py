#coding=utf-8

import pymysql
db = pymysql.connect("192.168.1.74","root","password","yuangg")
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
print("database version: %s" %data )
db.close()