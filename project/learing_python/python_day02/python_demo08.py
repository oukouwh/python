#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 21:04
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo08.py
# @Email : oukouwh@gmail.com
# @Software: PyCharm
'''
    方阵转置
'''
list_info = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
for i in range(1,len(list_info)):
    for j in range(i, len(list_info)):
        list_info[j][i-1],list_info[i-1][j] = list_info[i-1][j],list_info[j][i-1]
# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
print(list_info)