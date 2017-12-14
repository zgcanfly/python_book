#coding=utf-8
import command
import os
status="df -h"
diskinfo=os.system(status)
print(diskinfo)