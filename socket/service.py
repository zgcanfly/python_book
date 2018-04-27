#coding=utf-8
#创建TCP服务器
from socket import *
import os
from time import ctime
HOST='localhost'
# HOST=gethostname()
PORT=21567
BUFSIZ=4096
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM) #创服务器套接字
tcpSerSock.bind(ADDR) #套接字与地址绑定
tcpSerSock.listen(5)  #监听连接,传入连接请求的最大数

while True:
    print('waiting for connection...')
    tcpCliSock,addr =tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data =tcpCliSock.recv(BUFSIZ).decode()
        print('[%s] %s' %(ctime(),data))
        if not data:
            break
        cmd = os.popen(data)
        result=cmd.read()
        tcpCliSock.sendall(result.encode())
        # tcpCliSock.sendall(('[%s] %s' %(ctime(),str(data).upper())).encode())
        # tcpCliSock.send(('[%s] %s' %(ctime(),data)).encode())

    tcpCliSock.close()
tcpSerSock.close()