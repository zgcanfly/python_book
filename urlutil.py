#coding=utf-8

import  urllib.request as request
import  urllib.parse as parse
import string
import re
import os
import urllib.error as error




print("============================================")
def baidu_tieba(url,begin_page,end_page):
    count=1
    for i in range(begin_page,end_page + 1 ):
        sName = '/tmp/'+str(i).zfill(5)+'.html'
        print('正在下载 '+str(i)+'个页面，并保存为'+sName)
        m=request.urlopen(url+str(i)).read()
        dirpath = '/tmp/img'
        dirname = str(i)
        new_path = os.path.join(dirpath,dirname)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        #page_data = m.decode('GBK')
        page_data = m.decode('gbk',).encode('utf-8')
        page_image = re.compile('<img src=\"(.+?)\"')
        for image in page_image.findall(page_data):
            pattern = re.compile(r'^http://.*.png$')
            if pattern.match(image):
                try:
                    image_data = request.urlopen(image).read()
                    image_path = dirpath + dirname + '/'+str(count)+'.png'
                    count +=1
                    print(image_path)
                    with open(image_path,'wb') as image_file:
                        image_file.write(image_data)
                    image_file.close()
                except error.URLError as e:
                    print('Download failed')
            with open(sName,'wb') as file:
                file.write(m)
            file.close()
#        with open(sName,'wb') as file:
#            file.write(m)
#        file.close()

if __name__ == '__main__':
    url="http://tieba.baidu.com/p/"
    begin_page=1
    end_page=3
    baidu_tieba(url,begin_page,end_page)