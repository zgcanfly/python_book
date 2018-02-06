#coding=utf-8
import os
import mail
import sys
import psutil
import socket

default_disk="80%"
default_mem=1000
default_cpu="80%"

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
        mail.sendEmail(content)
    else:
        return disk_data

def check_mem():
    if (print_type == 1) or isset(sys.argv, "mem"):
        memory_convent = 1024 * 1024
        mem = psutil.virtual_memory()
        mem_data=int(mem.total / (memory_convent) - mem.used / (1024 * 1024))
    if mem_data < default_mem:
        content = hostname + "(" + ip + ")" + "：服务器内存值过低，请悉知"+"\n当前内存值为:"+str(mem_data)+"M"
        mail.sendEmail(content)

def check_cpu():
    Cpu_usage = psutil.cpu_percent()
    if Cpu_usage > int_value(default_cpu):
        content=hostname + "(" + ip + ")" + ":cpu利用率过高，请悉知"+"\n当前cpu利用率为:" +str(Cpu_usage)+"%"
        mail.sendEmail(content)
if __name__=='__main__':
    check_disk()
    check_mem()
    check_cpu()