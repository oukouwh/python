#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/6 21:19
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: tcp_server.py
# @Email : oukouwh@163.com
# @Software: PyCharm
import socket
from time import sleep

# 创建套接字
socket_link = socket.socket()

# 绑定地址
socket_link.bind(('0.0.0.0', 9011))

# 设置监听
socket_link.listen(8)

# 阻塞等待客户端连接
while True:
    print('正在加载，请稍后........')
    try:
        connfd, addr = socket_link.accept()
        print("Connect from", addr)  # 打印连接的客户端
    except KeyboardInterrupt:
        print("服务端退出")
        break
    except Exception as e:
        print(e)
        continue

        # 收发消息
    while True:
        data = connfd.recv(5)
        # 连接的客户端退出，recv会立即返回空字符串
        if not data:
            break
        print(data.decode())
        sleep(0.1)
        n = connfd.send(b"Thanks#")
        print("Send %d bytes" % n)
    connfd.close()

# 关闭套接字
socket_link.close()
