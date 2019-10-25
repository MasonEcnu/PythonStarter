#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 访问限制
# __双下划线表示私有


class Student(object):

    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def __print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_gender(self):
        self.__print_score()
        return self.__gender

    def set_gender(self, new_gender):
        if new_gender == "male" or new_gender == "female":
            self.__gender = new_gender
        else:
            raise ValueError('bad gender %s' % new_gender)


if __name__ == "__main__":
    bart = Student('Bart Simpson', 59, "female")
    bart._Student__name = "111"
    bart.__print_score()
    print(bart.get_gender())
    bart.set_gender("111")
