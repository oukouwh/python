#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 16:35
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_bank.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Bank:
    total_money = 100000000

    def __init__(self, name, money):
        self.name = name
        self.money = money
        Bank.total_money -= money


Bank('舍人支行', 20000)
Bank('千代田支行', 120000)

print('剩下%d円' % Bank.total_money)
