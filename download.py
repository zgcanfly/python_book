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

url = 'https://jp.pornhub.com'

ssl._create_default_https_context = ssl._create_unverified_context


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


def downfile(downurl,title):
    title=title+'.mp4'
    filename=os.path.basename(title)
    urllib.request.urlretrieve(downurl, filename, callbackfunc)


def getporhub():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    try:
        r = request.Request(url)
    except request.RequestException as e:
        print("网页失败请求！1")
    response=request.urlopen(r)
    try:
        html=response.read().decode('utf-8')
    except:
        pass
    rtitle=re.findall(r'<title>.*?</title>',html)
    rdownurl=re.findall(r'videoUrl.*?}',html)
    print("\n")
    rtitle=str(rtitle)
    title=re.sub('<.*?title>','',rtitle)
    title=re.sub('\[','',title)
    title=re.sub(']','',title)
    print(title)
    print("\n")
    for i in range(1):
        downurl = rdownurl[i].split('"')[2]
        downurl = re.sub('\\\\','',downurl)
        print(downurl)
    downfile(downurl,title)




def parse_ph_key(response):
    try:
        selector = Selector(text=response)
    except:
        pass
    divs = selector.xpath('//div[re:test(@class,"thumbnail-info-wrapper")]//@href').extract()
    for div in divs:
        viewurl = 'https://jp.pornhub.com/%s' % div
        print("viewurl:"+viewurl)

def start_url():
    try:
        r = request.Request(url=url)
    except request.RequestException as e:
        print("网页请求失败! 2")
    response = request.urlopen(r)
    try:
        response = response.read().decode('utf-8')
    except:
        pass
    # print(response)
    parse_ph_key(response)

if __name__=='__main__':
    # getporhub()
    start_url()
    # 启动线程下载
    # threading.Thread(target=downimg,args=('')).start()
