
# 把whatToSay传给除了exceptNum的所有人
import socket
import threading

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Buffercache=1024
# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

def recvThreadFunc():
    while True:
        try:
            otherword =connection.recv(Buffercache)
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
            connection.send(sendword)
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')

while True:
    # 建立客户端连接
    connection, addr = serversocket.accept()

    # print("连接地址: %" % str(addr))

    msg = '欢迎来到 Yuangg 管理区域！' + "\r\n"
    buf = connection.recv(1024).decode()
    if buf == '1':
        connection.send(msg.encode('utf-8'))
        connection.close()