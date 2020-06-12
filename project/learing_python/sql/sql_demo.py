#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/12 15:43
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: sql_demo.py
# @Email : oukouwh@163.com
# @Software: PyCharm
import pymysql

db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456A',
                     database = 'py_database'
                    )
cur = db.cursor()
sql = 'select * from userinfo'
cur.execute(sql)
# 获取多个查询结果
# data = cur.fetchmany(10)
# 获取单个查询结果
# data = cur.fetchone()
# 获取全部查询结果
data = cur.fetchall()
print(data)
db.close()
cur.close()