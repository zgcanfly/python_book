import urllib.request
from urllib import request
import sys
import os
import io
import ssl
import re
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from  bs4 import BeautifulSoup
# import threading
import pymongo
import time
import random
import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516572910651&di=378d48a3a4bc2791c973ab3abc6d5664&imgtype=0&src=http%3A%2F%2Fsrc.onlinedown.net%2Fd%2Ffile%2Fp%2F2017-01-17%2F6d12012fee7ab36a227e7ef807e96a1f.jpg'
ssl._create_default_https_context = ssl._create_unverified_context


#待完善功能
#1.更换header
#2.存取mongo数据



def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    global url
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    downsize=blocknum * blocksize
    if downsize >= totalsize:
       downsize=totalsize
    s ="%.2f%%"%(percent)+"====>"+"%.2f"%(downsize/1024/1024)+"M/"+"%.2f"%(totalsize/1024/1024)+"M \r"
    sys.stdout.write(s)
    sys.stdout.flush()
    if percent == 100:
        print('')
        input('输入任意键继续...')


def down_file():
    filename=os.path.basename('download\/'+url)
    request.urlretrieve(url, filename, callbackfunc)


if __name__=='__main__':
	down_file()
    # 启动线程下载
    # threading.Thread(target=downimg,args=('')).start()
