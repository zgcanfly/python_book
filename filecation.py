#coding=utf-8

import os, sys
path="README.md"
pwd=os.getcwd()
print(pwd)
fd=os.open(path,os.O_RDWR)
d_fd=os.dup(fd)
os.write(d_fd,"This is test")

os.closerange(fd,d_fd)
print("关闭所有文件")