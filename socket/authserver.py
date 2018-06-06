
import socket,os
# import threading
from time import  ctime

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

def PrintLog(logmessage,myconnection='',nickname='',bye=''):
    msg = '[' + ctime() + '] ' +nickname +' : '+ logmessage
    try:
        if not myconnection:

            print(msg)
        elif bye=='bye':
            myconnection.send('bye'.encode())
        else:
            myconnection.send(msg.encode())
            print(msg)
    except :
        pass

def subThreadIn(myconnection, connNumber,nickname):
            PrintLog('开始进入远程操控模式',myconnection)

            while True:
                try:
                    data=myconnection.recv(Buffercache).decode()
                    PrintLog(logmessage=data,nickname=nickname)
                    if not data:
                        break
                    elif data=="bye":
                        PrintLog("用户退出!",myconnection=myconnection,bye='bye')
                    cmd = os.popen(data)
                    result = cmd.read()
                    myconnection.sendall(result.encode())
                except (OSError,ConnectionResetError):
                    PrintLog("用户已经退出!")
                    myconnection.close()
                    break
            myconnection.close()


def authThreadIn(myconnection, connNumber):
        try:
            for i in {1,2,3}:
                PrintLog('等待验证',myconnection)
                nickname = myconnection.recv(Buffercache).decode()
                PrintLog('登入用户: '+nickname)
                authcode = myconnection.recv(Buffercache).decode()
                if authcode == key:
                    message='['+ctime()+'] '+nickname + " 验证成功"
                    print(message)
                    myconnection.send(message.encode())
                    return nickname
                else:
                    PrintLog('验证失败， 重新验证' + str(i) + '/3', myconnection)
                    if i == 3:
                        PrintLog('验证失败， 重新验证' + str(i) + '/3', myconnection, 'bye')
                        myconnection.close()
        except (OSError,ConnectionResetError):
            PrintLog("用户已经退出!")
            myconnection.close()


if __name__=='__main__':
    while True:
        # 建立客户端连接
        connection, addr = serversocket.accept()
        connection.send(msg.encode('utf-8'))
        buf = connection.recv(Buffercache).decode()

        if buf == '1':
            nickname=authThreadIn(connection,connection.fileno())
            subThreadIn(connection, connection.fileno(),nickname)