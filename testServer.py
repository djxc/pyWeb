# -*- coding: utf-8 -*-
import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)



if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # 创建socket
    s.bind(('127.0.0.1', 9999))     #socket绑定端口
    s.listen(5)     # socket监听的最大个数
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()