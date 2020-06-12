#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/2 20:15
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: data02.py
# @Email : oukouwh@163.com
# @Software: PyCharm
'''
    递归实现算法
'''
def fun_data(number):
    if number <= 1:
        return 1
    return number * fun_data(number - 1)

data = fun_data(5)
print(data)