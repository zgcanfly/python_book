# -*- coding: utf-8 -*-
import pymysql
import socket
import mail
import time
import pandas as pd



host = '106.15.224.237'
base = 'cortana'
passwd = 'password'
user = 'root'
base = 'cortana'
database = 'cortana'
tablename = 'weather'
hostname = socket.gethostname()
date=time.strftime("%F", time.localtime())

try:
    db = pymysql.connect(host, user, passwd, base, charset="utf8")
    cursor = db.cursor()
except:
    content = hostname+":Mysql数据库链接错误 ，请检查数据库状态"
    mail.sendEmail(content)



def createDB():
    db = pymysql.connect(host, user, passwd)
    cursor = db.cursor()
    createdbsql = "create database if not exists `" + base + "` DEFAULT CHARSET utf8 COLLATE utf8_general_ci;"
    try:
        cursor.execute(createdbsql)
        db.commit()
    except pymysql.Warning as e:
        print(e)
    except:
        db.rollback()
    results = cursor.fetchall()
    print(results)
    db.close()
def createTable():
    db = pymysql.connect(host, user, passwd, base, charset="utf8")
    cursor = db.cursor()
    createtablesql="create table "+tablename+" (id int(11) primary key auto_increment,date varchar(128),data varchar(128),wea nvarchar(128), message nvarchar(128)) engine = innodb auto_increment = 1 default charset=utf8"
    try:
        cursor.execute(createtablesql)
        db.commit()
    except:
        db.rollback()
    results=cursor.fetchone()
    print(results)
    db.close()

def insertDB(date,data,wea,message,name):
    db = pymysql.connect(host, user, passwd, base, charset="utf8")
    cursor = db.cursor()
    #下面两行要保持一致的结构
    column_str='date,data,wea,message,name'
    insert_str="'"+date+"','"+data+"','"+wea+"','"+message+"','"+name+"'"
    inserttsql="INSERT INTO weather(%s) VALUES(%s)"%(column_str,insert_str)
    try:
        cursor.execute(inserttsql)
        db.commit()
    except:
        db.rollback()
    db.close()
#插入单行数据时候可以使用db.close,多行时 不能在这里使用db.close
def selectDB():
    db = pymysql.connect(host, user, passwd, base, charset="utf8")
    cursor = db.cursor()

    list_ldate=[]
    list_ldata=[]
    list_lwea=[]
    list_lmessage=[]
    list_lname=[]
    insert_str="'"+date+"'"
    selectsql=" select * from weather where date=%s"%(insert_str)
    try:
        cursor.execute(selectsql)
        results = cursor.fetchall()

        for row in results:
            ldate = row[1]
            ldata = row[2]
            lwea = row[3]
            lmessage = row[4]
            lname = row[5]
            list_ldate.append(ldate)
            list_ldata.append(ldata)
            list_lwea.append(lwea)
            list_lmessage.append(lmessage)
            list_lname.append(lname)
        df = pd.DataFrame({
                           'date':list_ldata,
                           'wea':list_lwea,
                           'zero': list_lmessage,
                           'name':list_lname}
                           )
        return  df.get_values()
    except Exception as e:
        print(e)


