# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import smtplib

title = '来自小娜的天气预警'
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

