# -*- coding: utf-8 -*-
import re
import requests
from  bs4 import BeautifulSoup
import io
from email.mime.text import MIMEText
import sys
import smtplib
import pymysql
import time

url = 'http://www.weather.com.cn/weather/101020600.shtml'
content = '来自Cortana的空邮件'
title = '来自小娜的天气预警'
status = '雨'

host = '192.168.1.74'
base = 'yuangg'
passwd = 'password'
user = 'root'
base = 'cortana'
database = 'cortana'
tablename = 'weather'

#测试数据
date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
wea='雨'
message='雨'


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
    createtablesql="create table "+tablename+" (id int(11) primary key auto_increment,date varchar(128),wea varchar(128), message varchar(128)) engine = innodb auto_increment = 1 default charset=utf8"
    try:
        cursor.execute(createtablesql)
        db.commit()
    except:
        db.rollback()
    results=cursor.fetchone()
    print(results)
    db.close()

def insertDB(date,wea,message):
    inserttsql="INSERT INTO weather(date,wea,message) VALUES('"+date+"','"+wea+"','"+message+"')"
    try:
        cursor.execute(inserttsql)
        db.commit()
    except:
        db.rollback()
    db.close()



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
    #    print(rwea,rtemp1,rtemp2)
    for i in range(1):
        data = rdata[i].split('>')[1].split('<')[0]
        wea = rwea[i].split('>')[1].split('<')[0]
        temp1 = rtemp1[i].split('>')[1].split('<')[0]
        temp2 = rwea[i].split('>')[1].split('<')[0]
        tplt = "{0:^10}\t{1:{4}^10}\t{2:}\t{3:<}\t{4:}"
        water = tplt.format(data, wea, temp1, "~" + temp2, chr(12288))
        #邮件通知
        if status in wea:
            content = str(water) + "亲爱的主人 检测到天气有雨  出门请备伞!  出入平安哦～"
            sendEmail(content)
            #message=str(water)
            #wea=str(wea)
            #print(wea)
            #print(message)
            insertDB(date,wea,message)

if __name__ == '__main__':
    #weather()
    #createDB()
    #createTable()
    insertDB(date,wea,message)