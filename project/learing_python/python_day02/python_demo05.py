#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 10:01
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo05.py
# @Email : oukouwh01@gmail.com
# @Software: PyCharm
'''
    在控制台中录入一个字符串，判断是否为回文．
  判断规则:正向与反向相同．
  　　　上海自来水来自海上
'''
str_input = input('请输入字符串:')
if str_input == str_input[::-1]:
    print('是回文数')
else:
    print('不是回文数')