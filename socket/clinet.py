#coding=utf-8

from socket import *

HOST = 'localhost' #  or 'localhost'
PORT = 21567
BUFSIZ = 4096
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>:')
    #print('data=',data);
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

tcpCliSock.close()