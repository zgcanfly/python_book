#encoding=utf-8
# -*- coding: utf-8 -*-
import re
import requests
from  bs4 import BeautifulSoup
import io
import mail
import sys
import pymysql
import datetime
import time
import pandas as pd
import socket
#weather变量定义
#添加城市地址的url，具体url自己到中国气象网查询
urls={"上海":"http://www.weather.com.cn/weather/101020600.shtml","九江":"http://www.weather.com.cn/weather/101240201.shtml"}
content = '来自Cortana的空邮件'
status = '雨'
#数据库变量定义
host = '106.15.224.237'
base = 'cortana'
passwd = 'password'
user = 'root'
base = 'cortana'
database = 'cortana'
tablename = 'weather'

#测试变量定义
date=time.strftime("%F", time.localtime())
wea='雨'
message='0'
data='test'
name='上海'

hostname = socket.gethostname()

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
    #下面两行要保持一致的结构
    column_str='date,data,wea,message,name'
    insert_str="'"+date+"','"+data+"','"+wea+"','"+message+"','"+name+"'"
    inserttsql="INSERT INTO weather(%s) VALUES(%s)"%(column_str,insert_str)
    try:
        cursor.execute(inserttsql)
        db.commit()
    except:
        db.rollback()
#插入单行数据时候可以使用db.close,多行时 不能在这里使用db.close
def selectDB():
    list_ldate=[]
    list_ldata=[]
    list_lwea=[]
    list_lmessage=[]
    list_lname=[]
    insert_str="'"+date+"'"
    selectsql=" select * from weather where date=%s"%(insert_str)
    try:
        cursor.execute(selectsql)
    except:
        pass
    results=cursor.fetchall()
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



def weather(name,url):
    try:
        r = requests.get(url, timeout=30)
    except requests.RequestException as e:
        content = e + "天气url请求失败，请检查docker of cortana ！"
        mail.sendEmail(content)
    r.raise_for_status()
    r.encoding = 'utf-8'

    rdata = re.findall(r'<h1>.*?</h1>', r.text)
    rwea = re.findall(r'\"wea\">.*?</p>', r.text)
    rtemp1 = re.findall(r'\/<i>.*?</i>', r.text)
    rtemp2 = re.findall(r'<span>\d+\.?\d*</span>', r.text)
    # print(rdata,rwea,rtemp1,rtemp2)
    for i in range(6):
        data = rdata[i].split('>')[1].split('<')[0]
        wea = rwea[i].split('>')[1].split('<')[0]
        temp1 = rtemp1[i].split('>')[1].split('<')[0]
        temp2 = rwea[i].split('>')[1].split('<')[0]
        tplt = "{0:^10}\t{1:{4}^10}\t{2:}\t{3:<}\t{4:}"
        water = tplt.format(data, wea, temp1, "~" + temp2, chr(12288))
        # print(water)
        #邮件通知
        if status in water:
            message=str(temp1)
            wea=str(wea)
            data=str(data)
            try:
                # print(date,data,wea,message,name)
                insertDB(date,data,wea,message,name)

            except:
                content=hostname +": Mysql数据库插入data error ，请检查数据库状态"
                print(content)
                # mail.sendEmail(content)
    temp3 = selectDB()
    if status in temp3:
        content = "  亲爱的主人 检测到天气有雨  出门请备伞!  出入平安哦～\n %s " % (str(temp3))
        print(content)
        mail.sendEmail(content)
    else:
        print("天气为空")
if __name__ == '__main__':
    for name,url in urls.items():
        print(name,url)
        weather(name,url)
    db.close()
        #createDB()
    # createTable()
    # selectDB()
    # 修改表结构
    # alter table weather add column name varchar(64);