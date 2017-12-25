# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import smtplib
import jenkins
import time
title = 'cortana'
jenkins_server_url='http://jenkins.stockalert.cn'
jenkins_id='zgyang'
jenkins_token='f4f892e1871ae8b437ca4c990895b5ca'
server=jenkins.Jenkins(url=jenkins_server_url,username=jenkins_id,password=jenkins_token)
project=''


def deploy(project):
    server.build_job(project)
    info = server.get_job_info(project)['lastBuild']
    number = info['number']
    number += 1
    time.sleep(10)
    tinfo = server.get_build_info(project, number)
    return tinfo

def RemoveChinese(strValue):
    pass


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

def onQQMessage(bot, contact, member, content):
    #获取项目列表及发布列表
    project_list = []
    deploy_list = []
    joblist = server.get_all_jobs()
    for i in range(len(joblist)):
        project_list.append(joblist[i]['name'])
        deploy_list.append('发布'+joblist[i]['name'])

#文字聊天部分
    if content == '天气怎么样':
        bot.SendTo(contact, '今天天气不错，晚上可以看星星呢')
    elif content == 'hello':
        bot.SendTo(contact, '你好,我是cortana')
    elif content == '发邮件':
        sendEmail(content)
        bot.SendTo(contact, '什么邮件')
 #jenkins部分
    elif content == '项目列表':
        bot.SendTo(contact, str(project_list))
    elif content == '发布列表':
        bot.SendTo(contact, str(deploy_list))
    elif content == '测试发布':
        bot.SendTo(contact,str(project_list))
        bot.SendTo(contact,str(deploy_list))
#发布项目
    if content in deploy_list:
        project=content[2:]
        deploystatus = deploy(project)
        print(deploystatus['result'])
        if deploystatus['result'] == 'SUCCESS':
            bot.SendTo(contact, '项目发布成功')
        else:
            bot.SendTo(contact, '项目发布失败' + deploystatus['url'])


#生活小助手部分