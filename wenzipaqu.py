#coding=utf-8
import urllib
import urllib.request as request
from bs4 import BeautifulSoup
def taobao(url):
    response = request.urlopen(url)
    html = response.read()
    data=html.decode('gbk').encode('utf-8')
    soup=BeautifulSoup(data)
    for list in soup.find_all('h3'):
        print(list.string)
if __name__=='__main__':
    print("===================")
    url='http://www.taobao.com/?spm=a310q.2219005.1581860521.1.b9kUd4'
    taobao(url)