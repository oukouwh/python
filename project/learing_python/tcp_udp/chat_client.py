#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/7 20:27
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: chat_client.py
# @Email : oukouwh@163.com
# @Software: PyCharm
from socket import *
import os, sys

# 服务端地址
ADDRESS = ('127.0.0.1', 9828)


def send_msg(socket_link, name):
    while True:
        text = input('msg>>>>')
        msg = 'C %s %s' % (name, text)
        socket_link.sendto(msg.encode(), ADDRESS)


def recv_msg(socket_link):
    while True:
        data, addr = socket_link.recvfrom(1024)
        print(data.decode())


def main():
    socket_link = socket(AF_INET, SOCK_DGRAM)
    while True:
        str_name = input('请输入：')
        msg = 'login ' + str_name
        socket_link.sendto(msg.encode(), ADDRESS)
        data, addr = socket_link.recvfrom(1024)
        if data.decode() == '0':
            print('进入房间')
            break
        else:
            print('Error')
    pid = os.fork()
    if pid == 0:
        send_msg(socket_link, str_name)  # 子进程负责消息发送
    else:
        recv_msg(socket_link)  # 父进程负责消息接收


# main()
