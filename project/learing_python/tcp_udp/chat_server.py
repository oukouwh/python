#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/7 20:26
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: chat_server.py
# @Email : oukouwh@163.com
# @Software: PyCharm

from socket import *
import os, sys

ADDRESS = ('0.0.0.0', 9828)
user_info = {}

def do_chat(socket_link,name,text):
    msg = '%s: %s'%(name,text)
    for i in user_info:
        if i != name:
            socket_link.sendto(msg.encode(),user_info[i])

def do_request(socket_link):
    while True:
        data, addr = socket_link.recvfrom(1024)
        temp = data.decode().split(' ')
        if temp[0] == 'login':
            do_login(socket_link,temp[1],addr)
        elif temp[0] == 'C':
            text = ' '.join(temp[2:])
            do_chat(socket_link,temp[1],)


def do_login(scoket,name,address):
    if name in user_info:
        scoket.sendto('该用户已存在'.encode(),address)
        return
    scoket.sendto(b'0',address)
    msg = '%s进入聊天'%name
    for i in user_info:
        scoket.sendto(msg.encode(),user_info[i])
    user_info[name] = address

def main():
    socket_link = socket(AF_INET, SOCK_DGRAM)
    socket_link.bind(ADDRESS)

    # 请求处理函数
    do_request(socket_link)


main()
