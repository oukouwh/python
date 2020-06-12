#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 20:15
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo01.py
# @Email : oukouwh01@gmail.com
# @Software: PyCharm
'''
    数据类型
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''
# Number（数字）
int_num = 123
print(int_num) # 123

# String（字符串）
str_order = '订单详情'
print(str_order) # 订单详情

# List（列表）
list_info = [1,23,4,5,6]
print(list_info) #[1, 23, 4, 5, 6]
# 查找
print(list_info[0]) # 1
# 修改
list_info[0] = 'ABC' # ['ABC', 23, 4, 5, 6]
# 增加
list_info.append('TED')
list_info.insert(1,'改变数据成功')
# 删除
list_info.remove('ABC')
# 步长
print(list_info[0:4:2])
print(list_info)
for i in list_info:
    print(i)
# ABC
# 23
# 4
# 5
# 6

# Tuple（元组）
'''
    元组可以被索引和切片
    元组的元素不能修改
    元组可以使用+操作符进行拼接
'''
tuple_info = (1,2,3,4,5)
print(tuple_info) # (1, 2, 3, 4, 5)
for i in tuple_info:
    print(i)

# 查找
print(tuple_info[0]) # 输出元组的第一个元素
# 元组不可修改
# tuple_info[0] = 99
# print(tuple_info[0])
# TypeError: 'tuple' object does not support item assignment

# Set（集合）
'''
    大括号{}或者set()函数创建集合
    创建一个空集合必须用set()而不是{}因为{}是用来创建一个空字典
    set集合特点是去重复和无序排列
'''
set_info = set() #创建方式1
print(set_info) # set()
set_info = {'A','A','B','C'} # 创建方式2
print(type(set_info)) # <class 'set'>
print(set_info) # {'B', 'C', 'A'}

# Dictionary（字典）
'''
    字典是无序的对象集合
    是一个无序的 键(key) : 值(value) 的集合。
    键(key)必须使用不可变类型
    同一个字典中键(key)必须是唯一的。
'''
dict_info = {'name': 'hello','age':1, 'address': 'www.google.com'}
print(dict_info)
print(dict_info.items())
for key,value in dict_info.items():
    print(key,value)
print(dict_info['name']) # 获取value

