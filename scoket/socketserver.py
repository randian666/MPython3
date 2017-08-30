#!/usr/bin/env python3

'''
scoket服务端
大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器
'''

# 导入socket库:
import socket,threading,time

# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1',9999))
# 紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send('hi~你好!'.encode('utf-8')); #给客户端发送消息
    while True:
        data=sock.recv(1024)  #接受客户端消息
        print(data.decode('utf-8'))
        time.sleep(1);
        if  not data or data.decode('utf-8')=='exit':
            break;
        send_msg=input('please to input:')
        sock.send(send_msg.encode('utf-8')); #给客户端发送消息
    sock.close();
    print('Connection from %s:%s closed.' % addr)

while True:
    sock,addr=s.accept();
    # 创建新线程来处理TCP连接:
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start();


