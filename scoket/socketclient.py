#!/usr/bin/env python3

# 导入socket库
import socket,threading,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
#建立连接
s.connect(('127.0.0.1',9999))
msg=s.recv(1024).decode('utf-8')
print(msg)
while True:
    data=input("please input:")
    if((data.encode('utf-8')).decode('utf-8')=='exit'):
        break;
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
# for data in ['zhagnsan','lisi','李白']: #encode可以编码为指定的bytes
#     s.send(data.encode("utf-8"));#给服务端发送消息
#     print(s.recv(1024).decode('utf-8')) #接受消息
# s.send(b"exit")#发送退出连接消息
s.close();