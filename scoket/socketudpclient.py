#!/usr/bin/env python3

import socket

# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
for data in ['zhagnsan','lisi','李白']: #encode可以编码为指定的bytes
    s.sendto(data.encode('utf-8'),('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close();