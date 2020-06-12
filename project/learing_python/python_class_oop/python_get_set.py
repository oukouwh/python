#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/23 20:59
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_get_set.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Order:
    def __init__(self,name,age,sex,address):
        self.set_name(name)
        self.get_name()
        self.set_age(age)
        self.get_age()
        self.set_sex(sex)
        self.get_sex()
        self.set_address(address)
        self.get_address()


    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return  self.__name

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return  self.__age

    def set_sex(self,sex):
        self.__sex = sex

    def get_sex(self):
        return  self.__sex

    def set_address(self,address):
        self.__address = address

    def get_address(self):
        return  self.__address

result_bean = Order('夏雨荷',28,'女','山东省济南市')
result_bean.set_name('李清照')
print(result_bean.get_name())
print(result_bean.get_age())
print(result_bean.get_sex())
print(result_bean.get_address())

