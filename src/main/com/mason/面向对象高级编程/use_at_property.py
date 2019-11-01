#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用@property


class Student(object):

    def __init__(self, birth):
        self._birth = birth

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("分数必须是整形或者浮点数")
        if value < 0 or value > 100:
            raise ValueError("分数必须是[0..100]范围内的数字")

        self.score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 只读属性
    @property
    def age(self):
        return 2019 - self._birth


stu = Student(2011)


class Screen(object):

    # 不带_就爆炸
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


scr = Screen()
scr.height = 768
scr.width = 1024
print(scr.resolution)
