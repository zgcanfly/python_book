#coding:utf-8
import time,random,ssl
from threading import Thread
from queue import Queue
ssl._create_default_https_context=ssl._create_default_https_context
num_fetch_threads=2
enclosure_queue=Queue(20)

feed_urls = ['http:xxx/xxx',]



def downloadEnclosure(i,q):
    while True:
        print('%s:Looking for the next enclosure' %i)
        url=q.get()
        print('%s:Downloading:%s' %(i,url))
        #使用sleep代替真是的下载
        time.sleep(i+2)
        q.task_done()
for i in range(num_fetch_threads):
    worker = Thread(target=downloadEnclosure,args=(i,enclosure_queue))
    worker.setDaemon(True)
    worker.start()

for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries']:
        for enclosure in entry.get('enclosures', []):
            print('Queuing:', enclosure['url'])
            while True:
                try:
                    if not enclosure_queue.full():
                        enclosure_queue.put(enclosure['url'])
                    else:
                        time.sleep(random.random)
                except Exception as e:
                    print(e)

print('*** Main thread waiting')
enclosure_queue.join()
print('*** Done')