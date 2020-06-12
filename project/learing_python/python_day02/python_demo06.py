#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 10:08
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo06.py
# @Email : oukouwh01@gmail.com
# @Software: PyCharm
'''
    定义在控制台中打印二维列表的函数
[
    [1,2,3,44],
    [4,5,5,5,65,6,87]
    [7,5]
]

1 2 3 44
4 5 5 5 65 6 87
7 5
'''
list_info = [
    [1, 2, 3, 44],
    [4, 5, 5, 5, 65, 6, 87],
    [7, 5]
]
for i in list_info:
    for item in i:
        print(item, end=" ")
    print()
print(list_info)