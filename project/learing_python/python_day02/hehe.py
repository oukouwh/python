#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 20:09
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: hehe.py
# @Email : oukouwh@gmail.com
# @Software: PyCharm

print('\n'.join([''.join([('Love'[(x - y) % len('Love')]if((x * 0.05)**2 + (y * 0.1)**2 - 1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
