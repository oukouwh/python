#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/23 10:41
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_hero.py
# @Email : oukouwh@163.com
# @Software: PyCharm
class Hero:

    def __init__(self, name, life_value, attack_power, defense):
        self.name = name
        self.life_value = life_value
        self.attack_power = attack_power
        self.defense = defense

    def print_info(self):
        print('当前英雄%s,生命值%d,攻击力%d,防御力%d' % (self.name, self.life_value, self.attack_power, self.defense))


list_hero_info = [
    Hero('jnx', 1000, 900, 40),
    Hero('YAMADA', 0, 200, 5),
    Hero('JIN', 300, 100, 10),
    Hero('JOJO', 0, 300, 40)
]


def find_name():
    for item in list_hero_info:
        if item.name == 'JOJO':
            return item


name_info = find_name()
if name_info:
    name_info.print_info()
else:
    print('该名称不存在')


def find_count_life_value():
    list_value = []
    for item in list_hero_info:
        if item.life_value == 0:
            list_value.append(item)
    return list_value


value_info = find_count_life_value()
for i in value_info:
    i.print_info()


# 平均攻击力
def find_hero_attack_power():
    sum_attcak_power = 0
    for i in list_hero_info:
        sum_attcak_power += i.attack_power
    return sum_attcak_power / len(list_hero_info)


avg_attcak = find_hero_attack_power()
print(avg_attcak)


# 删除防御力小于10的英雄
def del_defense():
    for i in range(len(list_hero_info) - 1, -1, -1):
        if list_hero_info[i].defense < 10:
            del list_hero_info[i]


del_defense()
for i in list_hero_info:
    i.print_info()

# 每位英雄的攻击力+50
def set_attack_power():
    for i in list_hero_info:
        i.attack_power += 50


set_attack_power()
for i in list_hero_info:
    i.print_info()
