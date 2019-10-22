#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用__slots__
from types import MethodType


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class Student(object):
    # 定义一个特殊的__slots__变量，来限制该class实例能添加的属性(方法)
    __slots__ = ("name", "age", "set_age")
    pass


stu = Student()
stu.name = "Mason"
print(stu.name)


def set_age(self, age):
    self.age = age


# 给一个实例绑定的方法，对另一个实例是不起作用的
stu.set_age = MethodType(set_age, stu)

stu.set_age(15)
print(stu.age)


def set_score(self, score):
    self.score = score


Student.set_score = set_score
stu.set_score(90)

print(stu.score)
