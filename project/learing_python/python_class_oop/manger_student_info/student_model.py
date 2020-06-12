#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/24 14:45
# @Author : WH Python学的好，牢饭吃的饱。
# @FileName: student_model.py
# @Email : oukouwh@163.com
# @Software: PyCharm
'''
    学生管理系统
    数据模型类：StudentModel
    逻辑控制类：StudentManagerController
    视图展示类：StudentModelView

'''


class StudentModel:
    '''
        学生信息模型
    '''

    def __init__(self, id=0, name='', age=0, score=0):
        '''
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        '''
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


# 逻辑控制类：StudentManagerController
class StudentManagerController:
    '''
        业务逻辑处理
    '''

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, student):
        '''
            添加学生信息
        :param student:
        :return:
        '''
        student.id += 1
        self.stu_list.append(student)

    def remove_student(self, id):
        '''
            根据id删除学生信息
        :param id:
        :return:
        '''
        for i in self.__stu_list:
            if i.id == id:
                self.__stu_list.remove(i)
                return True
        return False

    def update_student(self, student):
        '''
            根据id修改学生信息
        :param student:
        :return:
        '''
        for i in self.__stu_list:
            if i.id == student.id:
                i.name = student.name
                i.age = student.age
                i.score = student.score
                return True
        return False

    def order_by_score(self):
        '''
            根据成绩进行排序
        :return:
        '''
        for item in range(len(self.__stu_list) - 1):
            for i in range(item + 1, len(self.__stu_list)):
                if self.__stu_list[item].score > self.__stu_list[i].score:
                    self.__stu_list[item], self.__stu_list[i] = self.__stu_list[i], self.__stu_list[item]


# 视图展示类：StudentModelView
class StudentModelView:

    def __init__(self):
        '''
            视图管理器绑定逻辑处理器的类
        '''
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__update_student()
        elif item == "5":
            self.__output_student_by_score()

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        '''
            输入学生信息，进行保存
        :return:
        '''
        id = int(input("请输入ID："))
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu_bean = StudentModel(id,name,age,score)
        self.__manager.add_student(stu_bean)

    def __output_students(self, list_output):
        '''
            进行列表数据的展示
        :param list_output:
        :return:
        '''
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        '''
            根据编号进行删除
        :return:
        '''
        id = int(input("请输入编号："))
        if self.__manager.remove_student(id):
            print('删除成功')
        else:
            print('删除失败Error')

    def __update_student(self):
        '''
            更新学生信息
        :return:
        '''
        bean = StudentModel()
        bean.id = int(input("请输入需要修改的学生编号:"))
        bean.name = input("请输入新的学生名称：")
        bean.age = int(input("请输入新的学生年龄："))
        bean.score = int(input("请输入新的学生成绩："))
        if self.__manager.update_student(bean):
            print('更新成功')
        else:
            print('更新失败Error')

    def __output_student_by_score(self):
        '''
            根据成绩进行排序
        :return:
        '''
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


view = StudentModelView()
view.main()