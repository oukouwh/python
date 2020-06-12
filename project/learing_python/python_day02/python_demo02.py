#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 21:42
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo02.py
# @Email : oukouwh01@gmail.com
# @Software: PyCharm
'''
    在控制台中获取年龄，
    如果小于０岁，打印输入有误
    如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
    如果一个人的年龄为2（含）～13岁，就打印一条消息，指出他是儿童。
    如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
    如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
    如果一个人的年龄超过65（含）岁～150岁，就打印一条消息，指出他是老年人。
    150岁以上，打印"那不可能"
'''
int_age = int(input('请输入年龄:'))
if int_age < 2:
    print('婴儿')
elif int_age >= 13 and int_age <= 20:
    print('青少年')
elif int_age > 20 and int_age <= 65:
    print('青年')
elif int_age > 65 and int_age <= 150:
    print('老年人')
else:
    print('未知错误')
