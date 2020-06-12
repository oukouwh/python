#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 10:21
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: time_test.py
# @Email : oukouwh@163.com
# @Software: PyCharm
import time


def get_week(year, month, day):
    '''
        获取星期数
    :param year: 年
    :param month: 月
    :param day: 日
    :return:
    '''
    tuple_time = time.strptime('%d/%d/%d' % (year, month, day), '%Y/%m/%d')
    dict_weeks = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日',
    }
    return dict_weeks[tuple_time[6]]


result = get_week(2020, 5, 30)
print(result)


def bsty(year, month, day):
    '''
        根据输入时间计算活了多少天
    :param year: 年
    :param month: 月
    :param day: 日
    :return:
    '''
    tuple_param = time.strptime('%d/%d/%d' % (year, month, day), '%Y/%m/%d')
    lift_second = time.time() - time.mktime(tuple_param)
    return int(lift_second / 60 / 60 // 24)


result = bsty(1995, 8, 28)
print(result)
