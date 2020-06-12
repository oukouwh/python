#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 21:49
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_demo03.py
# @Email : oukouwh01@gmail.com
# @Software: PyCharm
'''
    根据身高体重,参照BMI,返回身体状况.
     BMI:用体重千克数除以身高米数的平方得出的数字
     中国参考标准
     体重过低BMI<18.5
     正常范围18.5≤BMI<24
     超重24≤BMI<28
     I度肥胖28≤BMI<30
     II度肥胖30≤BMI<40
     Ⅲ度肥胖BMI≥40.0
'''
int_height = int(input('請輸入身高:'))
int_weight = int(input('請輸入体重:'))
BMI_height = int_height / 100
BMI_info = int_weight / (BMI_height * BMI_height)
print(BMI_info)
if BMI_info < 18.5:
    print('体重过低')
elif 18.5 <= BMI_info and BMI_info < 24:
    print('正常范围')
elif 24 <= BMI_info and BMI_info < 28:
    print('超重')
elif 28 <= BMI_info and BMI_info < 30:
    print('I度肥胖')
elif 30 <= BMI_info and BMI_info < 40:
    print('II度肥胖')
elif BMI_info >= 40:
    print('Ⅲ度肥胖')