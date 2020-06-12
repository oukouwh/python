#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/24 9:36
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_person_property_set.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Person:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def ad(self):
        return self.__ad

    @ad.setter
    def ad(self, ad):
        if 10 <= ad <= 50:
            self.__ad = ad
        else:
            raise ValueError('超出设定范围，请重试')

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        if 100 <= hp <= 200:
            self.__hp = hp
        else:
            raise ValueError('设置错误')


person_bean = Person('Alex', 20, 150)
person_bean.name = 'mogener'
print(person_bean.name)
print(person_bean.ad)
print(person_bean.hp)
