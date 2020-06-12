#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/10 18:07
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: test_demo.py
# @Email : oukouwh@163.com
# @Software: PyCharm

cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
#
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
#
c=dict()
n=0
for i in cars:
    for a,b in locals.items():
        if i[0] == a:
            n += 1
            c[b] = n
print(c)