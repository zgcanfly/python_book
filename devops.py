#coding=utf-8


import os,sys,stat
path="/tmp/test.txt"


def changedir():
    retovl=os.getcwd()
    print("当前为止是:%s"%retovl)

    os.chdir(path)
    retovl=os.getcwd()
    print("现在位置是:%s"%retovl)

def accessdir():
    fet = os.access("/opt/sg_deploy",os.F_OK)
    ret = os.access("/opt/sg_deploy",os.R_OK)
    wet = os.access("/opt/sg_deploy",os.W_OK)
    xet = os.access("/opt/sg_deploy",os.X_OK)
    print(ret,fet,wet,xet)



def chflagsdir():
    flags = stat.UF_APPEND
    retovl=os.chflags(path,flags)
    print(retovl)



#chflagsdir()
#accessdir()

