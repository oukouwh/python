#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 22:32
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: python_order.py
# @Email : oukouwh@163.com
# @Software: PyCharm
'''
    订单支付系统
    订单号
    商品名
    商品价格
    商品数量
    支付金额
    找零

'''
class Order():
    def __init__(self,code,name,price,count,pay_price,dib=0):
        self.code = code
        self.name = name
        self.price = price
        self.count = count
        self.pay_price = pay_price
        self.dib = dib

    # 结算函数
    def settlement(self):
        # 支付金额减去购买商品的金额
        self.dib = self.pay_price - self.count * self.price
        print('商品的编号为%s,商品名为%s,商品价格为%.2f,商品数量为%d,支付金额%.2f,'
              '找零金额%.2f:'%(self.code,self.name,self.price,self.count,self.pay_price,self.dib))

order_info = Order('A01','日用品',20.4,5,200)
order_info.settlement()