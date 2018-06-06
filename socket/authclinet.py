# -*- coding: utf-8 -*-
# 导入 socket、sys 模块
import socket
import sys
import threading
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

def authThreadIn():
    s.send(b'1')
    nickName = input('input your nickname: ')
    s.send(nickName.encode())

    authcode = input('input your authcode: ')
    s.send(authcode.encode())

    print(s.recv(1024).decode())



def sendThreadFunc():
    while True:
        try:
            data = input(">:")
            s.send(data.encode())
        except ConnectionAbortedError:
            print('Server closed this connection!')
            exit()
        except ConnectionResetError:
            print('Server is closed!')
            exit()


def recvThreadFunc():
    while True:
        try:
            data = s.recv(Buffercache).decode()
            print(": ",data)
            if data == 'bye':
                print('服务器关闭链接，程序退出')
                exit()
        except ConnectionAbortedError:
            print('Server closed this connection!')
            exit()
        except ConnectionResetError:
            print('Server is closed!')
            exit()


if __name__=='__main__':
    authThreadIn()
    while True:
        th1 = threading.Thread(target=sendThreadFunc)
        th2 = threading.Thread(target=recvThreadFunc)
        threads = [th1, th2]

        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()