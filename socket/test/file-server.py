# _*_ coding:utf-8 _*_

from socket import *
import _thread

def tcplink(skt,addr):
    print(skt)
    print(addr,"已经连接上...")
    print('开始发送文件')
    with open('./ww.jpg', 'rb') as f:
        for data in f:
            print(data)
            skt.send(data)
    f.close()
    skt.close()


HOST = "127.0.0.1"
PORT = 23333
ADDR = (HOST,PORT)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

while True:
    print("等待连接...")
    skt,addr = server.accept()
    print(skt)
    try:
        _thread.start_new_thread(tcplink,(skt,addr))
    except:
        print("线程无法启动")
server.close()