# -*- coding: utf-8 -*-
import socket
import threading

# 使用socket进行网络链接

def connectSina():    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # 创建socket
    s.connect(('www.sina.com.cn', 80))      # 与服务器建立链接
    s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n')      #发送请求
    
    buffer = []
    
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
        
    data = b''.join(buffer)    
    
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header)
    #print(h)

def connectLocalhost():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # 创建socket
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__ == "__main__":
    for i in range(7):
        
        t = threading.Thread(target=connectLocalhost)
        t.start()
