#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/24 10:37
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: person_bank.py
# @Email : oukouwh@163.com
# @Software: PyCharm
'''
    小明在招商银行取钱
'''


class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money


class Bank:
    def __init__(self, name, money):
        self.__name = name
        self.__money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    def draw_money(self,person,money):
        self.money -= money
        person.money += money
        print(person.name+ '取了%d钱'%money)

person_info = Person('Alex',0)
bank_info = Bank('ICBC',10000)
bank_info.draw_monqey(person_info,1000)

# 青岛市市北区敦路539号金港花园
# 178 5310 3867