#coding=utf-8

import pymysql


host='192.168.1.74'
base='yuangg'
passwd='password'
user= 'root'


database=base
tablename="testtable"
id,deptId,salary='1','22','50'
name='zgyang'
db=pymysql.connect(host,user,passwd,base)
cursor=db.cursor()
def createdatabase():
    createdatabasesql="create database if not exists `"+database+"` default character set gbk collate gbk_chinese_ci"
    try:
        cursor.execute(createdatabasesql)
        db.commit()
    except:
        db.rollback()
    results=cursor.fetchall()
    print(results)
    db.close()

def createtable():
    createtablessql="create table "+tablename+" (id int(11) primary key,name varchar(25),deptId int(11),salary float)"
    try:
        cursor.execute(createtablessql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchone()
    print(results)
    db.close()

def insertdata():
    insertdatasql="insert into yuangg VALUES(%d,%s,%d,%d)"
    try:
        cursor.execute(insertdatasql,('1','zgyang','22','50'))
    except:
        print("insert faild")
    results = cursor.fetchall()
    print(results)
    db.close()

def dropdatabase():
    dropdatabasesql="drop database "+database
    try:
        cursor.execute(dropdatabasesql)
        db.commit()
    except:
        db.rollback()
        print("please ensure database ")
    results=cursor.fetchone()
    print(results)

def showdatabase():
    showdatabasesql='show databases'
    try:
        cursor.execute(showdatabasesql)
    except:
        print("Can't connect MySQL server ")
    results=cursor.fetchone()
    print(results)

def selectdata():
    selectdatasql="select * from " + tablename
    try:
        cursor.execute(selectdatasql)
    except:
        print("Can't select mysql table ")
    results=cursor.fetchall()
    print(results)


#createdatabase()
#createtable()
#insertdata()
#dropdatabase()
#showdatabase()

selectdata()