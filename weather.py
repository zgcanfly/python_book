# -*- coding: utf-8 -*-
import re
import requests
import mail
import time
import socket
import wrmysql
#weather变量定义
#添加城市地址的url，具体url自己到中国气象网查询
urls={"上海":"http://www.weather.com.cn/weather/101020600.shtml","九江":"http://www.weather.com.cn/weather/101240201.shtml"}
content = '来自Cortana的空邮件'
status = '雨'
date=time.strftime("%F", time.localtime())


wea='雨'
message='0'
data='test'
name='上海'

hostname = socket.gethostname()


def weather(name,url):
    try:
        r = requests.get(url, timeout=30)
    except Exception as e:
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
                print(date,data,wea,message,name)
                wrmysql.insertDB(date,data,wea,message,name)
                print("数据插入成功 !")
            except Exception as e:
                content=hostname +": Mysql数据库插入data error ，请检查数据库状态"
                print(content)
                mail.sendEmail(content)

def sendweather():
    temp3 = wrmysql.selectDB()
    temp4 = str(temp3)
    if status in temp4:
        content = "  亲爱的主人 检测到天气有雨  出门请备伞!  出入平安哦～\n %s " % (temp4)
        print(content)
        mail.sendEmail(content)
    else:
        print("天气为空")


if __name__ == '__main__':
    for name,url in urls.items():
        print(name,url)
        weather(name,url)
    sendweather()









    # createDB()
    # createTable()
    # selectDB()
    # 修改表结构
    # alter table weather add column name varchar(64);