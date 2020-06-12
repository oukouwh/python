#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/2 22:37
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: bubble.py
# @Email : oukouwh@163.com
# @Software: PyCharm
'''
    冒泡排序
'''


def bubble(list_info):
    for i in range(len(list_info) - 1):
        for j in range(len(list_info) - 1 - i):
            if list_info[j] > list_info[j + 1]:
                list_info[j], list_info[j + 1] = list_info[j + 1], list_info[j]


def sub_sort(list_info, start_index, end_index):
    x = list_info[start_index]
    while start_index < end_index:
        while list_info[end_index] >= x and end_index > start_index:
            end_index -= 1
        list_info[start_index] = list_info[end_index]
        while list_info[start_index] < x and start_index < end_index:
            start_index += 1
        list_info[end_index] = list_info[start_index]
    list_info[start_index] = x
    return start_index


'''
    快速排序
'''


def quick(list_info, start_index, end_index):
    if start_index < end_index:
        list_ = sub_sort(list_info, start_index, end_index)
        quick(list_info, start_index, list_ - 1)
        quick(list_info, list_ + 1, end_index)


data = [23, 43, 1, 32, 45, 6, 88]
# bubble(l)
quick(data, 0, len(data) - 1)
print(data)
