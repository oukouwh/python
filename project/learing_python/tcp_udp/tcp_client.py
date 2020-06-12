#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/6 21:08
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: tcp_client.py
# @Email : oukouwh@163.com
# @Software: PyCharm

from socket import *

# 创建套接字
socket_link = socket()

# 连接服务器
server_address = ('127.0.0.1',9011)
# 连接
socket_link.connect(server_address)


while True:
    # 发消息
    data = input('Msg:')
    if not data:
        break
    # 转换为字节串进行发送
    socket_link.send(data.encode())
    data = socket_link.recv(1024)
    # 打印字符串
    print('Server_send_data>>>>',data.decode())

# 关闭套接字
socket_link.close()
