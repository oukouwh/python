#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 22:21
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_class.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Person_info():
    # 数据成员
    def __init__(self,username,address,sex,age):
        # self 是调用当前方法的对象地址
        self.username = username
        self.address = address
        self.sex = sex
        self.age = age
    # 行为成员
    def say(self):
        print(self.username,self.address,self.sex,self.age)


# 实例化对象
person = Person_info('TT','上海','女',18)
person.say()