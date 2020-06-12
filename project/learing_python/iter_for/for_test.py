#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 19:59
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: for_test.py
# @Email : oukouwh@163.com
# @Software: PyCharm

tuple_info = ('A', 'B', 'C', 'D')
tuple_item = tuple_info.__iter__()
while True:
    try:
        item = tuple_item.__next__()
        print(item)
    except Exception:
        break


dict_info = {'AA': 1, 'BB': 2, 'CC': 3, 'DD': 4}
dict_item = dict_info.__iter__()
while True:
    try:
        item = dict_item.__next__()
        print(item)
    except Exception:
        break

