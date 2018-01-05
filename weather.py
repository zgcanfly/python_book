#encoding=utf-8
# -*- coding: utf-8 -*-
import re
import requests
from  bs4 import BeautifulSoup
import io
import smtplib
from email.mime.text import MIMEText
import sys
import pymysql
import datetime
import time
import pandas as pd
#weather变量定义
url = 'http://www.weather.com.cn/weather/101020600.shtml'
content = '来自Cortana的空邮件'
title = '来自小娜的天气预警'
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


db = pymysql.connect(host,user,passwd,base,charset="utf8")
cursor = db.cursor()

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

def insertDB(date,data,wea,message):
    column_str='date,data,wea,message'
    insert_str="'"+date+"','"+data+"','"+wea+"','"+message+"'"
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
        list_ldate.append(ldate)
        list_ldata.append(ldata)
        list_lwea.append(lwea)
        list_lmessage.append(lmessage)
    # df = pd.DataFrame({'':list_ldata,'天气':list_lwea,'信息':list_lmessage})
    df = pd.DataFrame({
                       'date':list_ldata,
                       'wea':list_lwea,
                       'zero':list_lmessage})
    return  list(df)

def sendEmail(content):  # 定义邮件报警
    mail_host = "smtp.163.com"
    mail_user = "15180641712@163.com"
    mail_pass = "yang1462295175"
    sender = '15180641712@163.com'
    receivers = ['2467815216@qq.com']
    message = MIMEText(content, 'plain', 'utf-8')  # 内容，格式，编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # ssl
        smtpObj.login(mail_user, mail_pass)  # 登入验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send success")
    except smtplib.SMTPException as e:
        print(e)


def weather():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    try:
        r = requests.get(url, timeout=30)
    except requests.RequestException as e:
        content = e + "天气url请求失败，请检查docker of cortana ！"
        sendEmail(content)
    r.raise_for_status()
    r.encoding = 'utf-8'

    rdata = re.findall(r'<h1>.*?</h1>', r.text)
    rwea = re.findall(r'\"wea\">.*?</p>', r.text)
    rtemp1 = re.findall(r'\/<i>.*?</i>', r.text)
    rtemp2 = re.findall(r'<span>\d+\.?\d*</span>', r.text)
    for i in range(6):
        data = rdata[i].split('>')[1].split('<')[0]
        wea = rwea[i].split('>')[1].split('<')[0]
        temp1 = rtemp1[i].split('>')[1].split('<')[0]
        temp2 = rwea[i].split('>')[1].split('<')[0]
        tplt = "{0:^10}\t{1:{4}^10}\t{2:}\t{3:<}\t{4:}"
        water = tplt.format(data, wea, temp1, "~" + temp2, chr(12288))
        #邮件通知
        if status in wea:
           # content =  data +temp1+ "   亲爱的主人 检测到天气有"+wea+"  出门请备伞!  出入平安哦～"
            message=str(temp1)
            wea=str(wea)
            data=str(data)
            insertDB(date,data,wea,message)
    temp3=selectDB()
    content = "   亲爱的主人 检测到天气有雨   出门请备伞!  出入平安哦～ %s "%(str(temp3))
    # content = "   亲爱的主人 检测到天气有" + wea + "  出门请备伞!  出入平安哦～ %s "%(str(temp3))
    print(content)
    sendEmail(content)
    db.close()
if __name__ == '__main__':
    weather()
    #createDB()
    # createTable()
    # selectDB()