
# 把whatToSay传给除了exceptNum的所有人
import socket
import threading

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Buffercache=1024
# 获取本地主机名
host = socket.gethostname()

port = 9999
key = '1111'
msg = '欢迎来到 Yuangg 管理区域！' + "\r\n"

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
mydict = dict()
mylist = list()
def tellOthers(exceptNum, whatToSay):
    for c in mylist:
        if c.fileno() != exceptNum:
            try:
                c.send(whatToSay.encode())
            except:
                pass


def subThreadIn(myconnection, connNumber):
    pass


def authThreadIn(myconnection, connNumber):
    print(connection)
    nickname = myconnection.recv(1024).decode()
    authcode = myconnection.recv(1024).decode()
    print(nickname)
    if authcode == key:
        message=nickname +" 验证成功"
        myconnection.send(message.encode())
    return


while True:
    # 建立客户端连接
    connection, addr = serversocket.accept()
    connection.send(msg.encode('utf-8'))
    buf = connection.recv(1024).decode()

    if buf == '1':
        print(connection)
        authThreadIn(connection,connection.fileno())