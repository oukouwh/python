#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/23 21:13
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_person.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Person:
    def __init__(self, name, ad, hp):
        self.set_name(name)
        self.set_ad(ad)
        self.set_hp(hp)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_ad(self, ad):
        if 10 <= ad <= 50:
            self.__ad = ad
        else:
            raise ValueError('超出设定范围，请重试')

    def get_ad(self):
        return self.__ad

    def set_hp(self, hp):
        if 100 <= hp <= 200:
            self.__hp = hp
        else:
            raise ValueError('设置错误')

    def get_hp(self):
        return self.__hp


person_bean = Person('Alex', 30, 200)
person_bean.set_hp(123)
print(person_bean.get_name())
print(person_bean.get_ad())
print(person_bean.get_hp())
