#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/24 8:56
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_person_property.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Person:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def set_name(self, name):
        self.__name = name


    def get_name(self):
        return self.__name

    name = property(get_name,set_name)

    def set_ad(self, ad):
        if 10 <= ad <= 50:
            self.__ad = ad
        else:
            raise ValueError('超出设定范围，请重试')

    def get_ad(self):
        return self.__ad

    ad = property(get_ad,set_ad)

    def set_hp(self, hp):
        if 100 <= hp <= 200:
            self.__hp = hp
        else:
            raise ValueError('设置错误')

    def get_hp(self):
        return self.__hp

    hp = property(get_hp,set_hp)


person_bean = Person('Alex', 30, 200)
person_bean.name = 'mogen'
print(person_bean.name)
print(person_bean.ad)
print(person_bean.hp)