#coding=utf-8
import os
import string
from multiprocessing import cpu_count
from email.mime.text import MIMEText
import sys
import psutil
import socket
import smtplib

default_disk="10%"
default_mem=3000

content = '来自火星的空邮件'
title = 'Pdt服务器预警'
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)



if len(sys.argv)==1:
    print_type =1
else:
    print_type=2

def isset(list_arr,name):
    if name in list_arr:
        return True
    else:
        return False

def sendEmail(content):#定义邮件报警
    mail_host = "smtp.163.com"
    mail_user = "15180641712@163.com"
    mail_pass = "yang1462295175"
    sender = '15180641712@163.com'
    receivers = ['2467815216@qq.com']
    message = MIMEText(content,'plain','utf-8')#内容，格式，编码
    message['From']="{}".format(sender)
    message['To']=",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj=smtplib.SMTP_SSL(mail_host,465)#ssl
        smtpObj.login(mail_user,mail_pass)#登入验证
        smtpObj.sendmail(sender,receivers,message.as_string()) #发送
        print("mail has been send success")
    except smtplib.SMTPException as e:
        print(e)

def int_value(string):
    if "%" in string:
        newint = int(string.strip("%"))/100
        return newint
    elif isinstance(string,int):
        return string
    else:
        print("数值错误")


def check_disk():
    str_data = os.popen('df -h|grep -w "/"').read()  # 获取/磁盘信息
    str_data = str_data.split()  # 转换为列表
    disk_data = str_data[4]  # 获取磁盘使用率

    if int_value(disk_data) > int_value(default_disk):
        content=hostname + "(" + ip + ")" + "：磁盘利用率过高，请悉知"+"\n当前磁盘利用率为:"+str(disk_data)
        sendEmail(content)
    else:
        return disk_data

def check_mem():
    if (print_type == 1) or isset(sys.argv, "mem"):
        memory_convent = 1024 * 1024
        mem = psutil.virtual_memory()
        mem_data=int(mem.total / (memory_convent) - mem.used / (1024 * 1024))
    if mem_data < default_mem:
        content = hostname + "(" + ip + ")" + "：服务器内存值过低，请悉知"+"\n当前内存值为:"+str(mem_data)
        sendEmail(content)

def check_cpu():
    str_data = os.popen('')
if __name__=='__main__':
    check_disk()
    check_mem()