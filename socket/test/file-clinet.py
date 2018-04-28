# _*_ utf-8 _*_

from socket import *

HOST = "127.0.0.1"
PORT = 23333
ADDR = (HOST,PORT)

client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)

with open("./gg.jpg","ab") as f:
    while True:
        data = client.recv(1024)
        if not data:
            break;
        f.write(data)

f.close()
print("接收完毕")
client.close()