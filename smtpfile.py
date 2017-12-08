#coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText

#第三方SMTP服务
mail_host = "smtp.163.com"
mail_user = "15180641712@163.com"
mail_pass = "yang1462295175"

sender = '15180641712@163.com'
receivers = [2467815216@qq.com]

content='我用python'
title='人生苦短'

def sendEmail():
    message = MIMEText(content,'plain','utf-8')
    message['From']="{}".format(sender)
    message['To']=",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj=smtplib.SMTP_SSL(mail_host),