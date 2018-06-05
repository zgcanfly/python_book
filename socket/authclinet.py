# -*- coding: utf-8 -*-
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 

# 设置端口好
port = 9999
Buffercache=1024
# 连接服务，指定主机和端口
s.connect((host, port))
print(s.recv(1024).decode())

s.send(b'1')
nickName = input('input your nickname: ')
authcode = input('input your authcode: ')
# s.send(b'2')
s.send(nickName.encode())
s.send(authcode.encode())
print(s.recv(1024).decode())

def recvThreadFunc():
    while True:
        try:
            otherword =s.recv(Buffercache)
            if otherword:
                print(otherword)
            else:
                pass
        except ConnectionAbortedError:
            print('Server closed this connection!')

        except ConnectionResetError:
            print('Server is closed!')


def sendThreadFunc():
    while True:
        try:
            sendword= input('>: ')
            s.send(sendword)
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')


# 接收小于 1024 字节的数据
# msg = s.recv(1024)
#
# s.close()
#
# print (msg.decode('utf-8'))