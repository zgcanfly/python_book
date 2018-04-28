# coding: utf-8

from socket import *
import json, time, threading
config = {
    'HOST': 'localhost',
    'PORT': 11011,
    'LISTEN_CLIENT': 50,
    'KEY': '391f10fadc339e9ec5fa15af60030ac1',
    'SIZE': 2048,
    'TIME_OUT': 1000,
    'HEART_TIME': 5,
    'MAGIC_STRING': '258EAFA5-E914-47DA-95CA-C5AB0DC85B11',
    'HANDSHAKE_STRING': "HTTP/1.1 101 Switching Protocols\r\n" \
            "Upgrade:websocket\r\n" \
            "Connection: Upgrade\r\n" \
            "Sec-WebSocket-Accept: {1}\r\n" \
            "WebSocket-Location: ws://{2}/chat\r\n" \
            "WebSocket-Protocol:chat\r\n\r\n"
}


class Server():
    """
    服务端基类
    """
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((config['HOST'], config['PORT']))  # 监听端口
        self.sock.listen(config['LISTEN_CLIENT'])  # 监听客户端数量

        # 所有监听的客户端
        self.clients = {}
        self.thrs = {}
        self.users = {}
        self.stops = []

    # 监听客户端连接
    def listen_client(self):
        while 1:
            # 循环监听
            tcpClientSock, addr = self.sock.accept()
            address = addr[0] + ':' + str(addr[1])  # ip:port

            # 握手
            topInfo = tcpClientSock.recv(1024)
            headers = {}
            if not topInfo:
                tcpClientSock.close()
                continue

            header, data = topInfo.split('\r\n\r\n', 1)

            try:
                getInfo = header.split('\r\n')[0].split(' ')[1].split('/')[1:]
                if getInfo[0] == 'name':
                    self.users[address] = str(getInfo[1])
                else:
                    self.users[address] = '匿名用户'
            except:
                self.users[address] = '匿名用户'


            for line in header.split('\r\n')[1:]:
                key, val = line.split(': ', 1)
                headers[key] = val

            if 'Sec-WebSocket-Key' not in headers:
                tcpClientSock.close()
                continue

            import hashlib, base64
            sec_key = headers['Sec-WebSocket-Key']
            res_key = base64.b64encode(hashlib.sha1(sec_key + config['MAGIC_STRING']).digest())

            str_handshake = config['HANDSHAKE_STRING'].replace('{1}', res_key).replace('{2}', config['HOST'] + ':' + str(config['PORT']))
            tcpClientSock.send(str_handshake)

            # 握手成功 分配线程进行监听
            print(address+'进来了')

            self.clients[address] = tcpClientSock
            self.thrs[address] = threading.Thread(target=self.readMsg, args=[address])
            self.thrs[address].start()
            # print(self.clients)

    def readMsg(self, address):
        # print(self.clients)
        if address not in self.clients:
            return False

        client = self.clients[address]

        import select
        time_out = 0
        while 1:
            # print(len(self.clients))
            if address in self.stops:
                self.close_client(address)
                print(address + u'已经离开了系统！')
                break

            # 检测超时
            if time_out >= config['TIME_OUT']:
                self.close_client(address)
                break

            time_out += 5

            infds, outfds, errfds = select.select([client, ], [], [], 5)
            if len(infds) == 0:
                continue

            time_out = 0
            try:
                info = client.recv(1024)
            except:
                self.close_client(address)
                break

            if not info:
                continue

            if info == 'quit':
                self.close_client(address)
                break
            code_len = ord(info[1]) & 127
            if code_len == 126:
                masks = info[4:8]
                data = info[8:]
            elif code_len == 127:
                masks = info[10:14]
                data = info[14:]
            else:
                masks = info[2:6]
                data = info[6:]
            i = 0
            raw_str = ""
            for d in data:
                # print(masks, masks[i % 4])
                raw_str += chr(ord(d) ^ ord(masks[i % 4]))
                # print(raw_str)
                i += 1

            # 获取到输入的数据 向所有的客户端发送
            # 开启线程记录

            if raw_str:
                t1 = threading.Thread(target=self.send_data, args=[raw_str, address])
                t1.start()

    def send_data(self, data, address):
        import struct
        from urllib import unquote
        try:
            username = unquote(self.users[address])
        except:
            username = '匿名用户'
        if data:
            data = str('【'+username+'说】'+data)
        else:
            return False
        token = "\x81"
        length = len(data)
        if length < 126:
            token += struct.pack("B", length)
        elif length <= 0xFFFF:
            token += struct.pack("!BH", 126, length)
        else:
            token += struct.pack("!BQ", 127, length)

        # struct为Python中处理二进制数的模块，二进制流为C，或网络流的形式。
        data = '%s%s' % (token, data)
        try:
            for key, val in self.clients.iteritems():
                client = val
                try:
                    client.send(data)
                except:
                    self.close_client(key)
        except:
            pass

    def close_client(self, address):
        try:
            client = self.clients.pop(address)
            self.stops.append(address)
            client.close()
            del self.users[address]
        except:
            pass

        print(address+u'已经退出')

if __name__ == '__main__':
    c = Server()
    c.listen_client()