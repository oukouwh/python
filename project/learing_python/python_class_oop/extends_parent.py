#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/25 10:52
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: extends_parent.py
# @Email : oukouwh@163.com
# @Software: PyCharm
'''
    类的继承关系
'''
class Animal:
    def eat(self):
        print('进食')

class Dog(Animal):
    def say(self):
        print('叫')

class Brid(Animal):
    def fly(self):
        print('飞翔')

parent = Animal()
parent.eat()

dog = Dog()
dog.say()
dog.eat()