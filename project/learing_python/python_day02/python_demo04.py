#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 9:53
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo04.py
# @Email : oukouwh01@gmail.com
# @Software: PyCharm
'''
    在控制台中获取一个整数作为边长．
　　根据边长打印矩形．
   例如：４
       ****
       *  *
       *  *
       ****
'''
int_number = int(input('请输入:'))
print('*' * int_number)
for i in range(int_number - 2):
    print('*' + ' ' * (int_number-2) + '*')
print('*' * int_number)