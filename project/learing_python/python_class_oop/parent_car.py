#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/25 11:14
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: parent_car.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class Bycicle(Car):
    def __init__(self,brand,speed,price):
        super().__init__(brand,speed)
        self.price = price

car = Car('宝马',320)
print(car.brand,car.speed)
bycicle = Bycicle('RR',390,1000)
print(bycicle.speed)
print(bycicle.brand)
print(bycicle.price)
