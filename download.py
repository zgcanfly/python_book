import urllib.request
from urllib import request
import sys
import os
import io
import ssl
import re
from  bs4 import BeautifulSoup
import threading

url = 'https://jp.pornhub.com/view_video.php?viewkey=ph597ac889773f6'
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
def downimg(downurl):
    url='http://dlsw.baidu.com/sw-search-sp/soft/e7/10520/KanKan_V2.7.8.2126_setup.1416995191.exe'
    filename=os.path.basename(downurl)
    urllib.request.urlretrieve(downurl, filename, callbackfunc)


def getporhub():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    try:
        r = request.Request(url)
    except request.RequestException as e:
        print("网页失败请求！")
    response=request.urlopen(r)
    html=response.read().decode('utf-8')
    html.encode='utf-8'
    rscript=re.findall(r'<script>.*?</script>',html.text)
    rtitle=re.findall(r'<title>.*?</title>',html.text)
    print(rscript)
    print("\n")
    print(rtitle)
    # for i in range(4):


if __name__=='__main__':
    getporhub()
    # 启动线程下载
    # threading.Thread(target=downimg,args=('')).start()
