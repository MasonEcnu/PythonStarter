#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 实例属性和类属性
# Java中的普通属性和静态属性
# 相同名称的实例属性将屏蔽掉类属性


class Student(object):
    count = 0
    # 类属性
    school = "瑞泉中学"

    def __init__(self, name, age, gender):
        Student.count += 1
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print(self.school, self.name, self.age, self.gender)


stu1 = Student("Li Lei", 22, "女")
stu2 = Student("Mason", 12, "男")
stu1.print_info()
# 实例属性的优先级高于类属性
stu2.school = "华东师范大学"
stu2.print_info()
# 删除实例属性
del stu2.school
stu2.print_info()

print(Student.count)
