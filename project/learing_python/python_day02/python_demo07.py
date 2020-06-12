#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 13:47
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo07.py
# @Email : oukouwh01@gmail.com
# @Software: PyCharm
'''
    5.(扩展)计算一个字符串中的字符以及出现的次数.
# 思想：
# 逐一判断字符出现的次数.
# 如果统计过则增加１，如果没统计过则等于１.

abcdefce
a 1
b 1
c 2
d 1
e 2
f 1
'''
dict_info = {}
str_info = 'abcdefce'
for i in str_info:
    if i not in dict_info:
        dict_info[i] = 1
    else:
        dict_info[i] += 1
print(dict_info)