#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/31 16:30
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: data01.py
# @Email : oukouwh@163.com
# @Software: PyCharm
'''
    单链表的构建和功能操作
'''


# 创建节点
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkList:
    def __init__(self):
        self.head = Node(None)

    def init_list(self, list_):
        p = self.head
        for i in list_:
            p.next = Node(i)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head
        while p is not None:
            print(p.value)
            p = p.next

    #     判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 增加节点头部增加
    def add_node(self, value):
        # 生成节点
        node = Node(value)
        node.next = self.head.next
        self.head.next = node

    # 指定插入节点
    def insert_node(self, index, value):
        # 生成节点
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        # 插入节点
        node = Node(value)
        node.next = p.next
        p.next = node

    # 删除节点
    def remove(self, val):
        p = self.head
        if p.next and p.next.value != val:
            p = p.next
        if p.next is None:
            raise ValueError('val is not in LinkList')
        else:
            p.next = p.next.next

    # 获取节点值
    def get_index(self, index):
        p = self.head.next
        for i in range(index):
            if p is None:
                raise IndexError("index out of range")
            p = p.next
        return p.value


l = LinkList()
l.init_list([3, 45, 565, 7])
l.show()
