# -*- coding: utf-8 -*-
import re
import requests
from  bs4 import BeautifulSoup
import io
from email.mime.text import MIMEText
import sys
import smtplib
import pymysql

url = 'http://www.weather.com.cn/weather/101020600.shtml'
content = '来自Cortana的空邮件'
title = '来自小娜的天气预警'
status = '晴'

host = '192.168.1.74'
base = 'yuangg'
passwd = 'password'
user = 'root'
base = 'cortana'
database = 'cortana'
tablename = 'weather'

#测试数据
data='testdata'
wea='testwea'
message='testchr'


db = pymysql.connect(host, user, passwd, base)
cursor = db.cursor()

def createDB():
    createdbsql = "create database if not exists `" + database + "` default character set gbk collate gbk_chinese_ci"
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
    createtablesql="create table "+tablename+" (id int(11) primary key auto_increment,date varchar(25),wea varchar(25), message varchar(128))"
    try:
        cursor.execute(createtablesql)
        db.commit()
    except:
        db.rollback()
    results=cursor.fetchall()
    print(results)
    db.close()

def insertDB():
    inserttsql="INSERT INTO weather(data, wea, message) VALUES ( "+data+","+wea+","+message+" )"
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
    for i in range(6):
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
        insertDB()

if __name__ == '__main__':
    #weather()
    #CreateDB()
    #createTable()
    insertDB()