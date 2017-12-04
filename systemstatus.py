#coding=utf-8

import sys
import psutil
import time
import os


time_str =time.strftime("%Y-%m-%d",time.localtime())
file_name="./"+time_str+".log"

if os.path.exists(file_name)== False:
    os.mknod(file_name)
    handle=open(file_name,"w")
else:
    handle=open(file_name,"a")
#获取命令行参数
if len(sys.argv)==1:
    print_type =1
else:
    print_type=2

def isset(list_arr,name):
    if name in list_arr:
        return True
    else:
        return False
print_str="";

#获取系统内存使用情况
if (print_type==1) or isset(sys.argv,"mem"):
    memory_convent=1024*1024
    mem=psutil.virtual_memory()
    print_str+="内存状态如下:\n"
    print_str=print_str+"系统的内存容量为: "+str( mem.total/( memory_convent ) ) + " MB\n"
    print_str = print_str + "   系统的内存以使用容量为: " + str(mem.used / (memory_convent)) + " MB\n"
    print_str = print_str + "   系统可用的内存容量为: " + str(mem.total / (memory_convent) - mem.used / (1024 * 1024)) + "MB\n"
    print_str = print_str + "   内存的buffer容量为: " + str(mem.buffers / (memory_convent)) + " MB\n"
    print_str = print_str + "   内存的cache容量为:" + str(mem.cached / (memory_convent)) + " MB\n"

#获取cpu的相关信息
if (print_type==1) or isset(sys.argv,"cpu"):
    print_str+="cpu状态如下:\n"
    cpu_status=psutil.cpu_times()
    print_str = print_str + "   user = " + str(cpu_status.user) + "\n"
    print_str = print_str + "   nice = " + str(cpu_status.nice) + "\n"
    print_str = print_str + "   system = " + str(cpu_status.system) + "\n"
    print_str = print_str + "   idle = " + str(cpu_status.idle) + "\n"
    print_str = print_str + "   iowait = " + str(cpu_status.iowait) + "\n"
    print_str = print_str + "   irq = " + str(cpu_status.irq) + "\n"
    print_str = print_str + "   softirq = " + str(cpu_status.softirq) + "\n"
    print_str = print_str + "   steal = " + str(cpu_status.steal) + "\n"
    print_str = print_str + "   guest = " + str(cpu_status.guest) + "\n"


# 查看硬盘基本信息
if (print_type == 1) or isset(sys.argv, "disk"):
    print_str += " 硬盘信息如下:\n"
    disk_status = psutil.disk_partitions()
    for item in disk_status:
        print_str = print_str + "   " + str(item) + "\n"

# 查看当前登录的用户信息
if (print_type == 1) or isset(sys.argv, "user"):
    print_str += " 登录用户信息如下:\n "
    user_status = psutil.users()
    for item in user_status:
        print_str = print_str + "   " + str(item) + "\n"

print_str += "---------------------------------------------------------------\n"
print(print_str)
handle.write(print_str)
handle.close()
