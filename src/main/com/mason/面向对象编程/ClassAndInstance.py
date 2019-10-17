#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类和实例
# 类是抽象的模板
# 实例是根据类创建出来的一个个具体的“对象”


class Student(object):
    pass


# 同一个文件里有同名类，居然不报错
class Student(object):

    # 特殊方法“__init__”前后分别有两个下划线！！！
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 数据封装
    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "E"


# Python允许对实例变量绑定任何数据，动态绑定，不同实例数据不互通
if __name__ == "__main__":
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    bart.age = 10
    print(bart.age)
    print(bart.get_grade())
    lisa.print_score()
    print(lisa.get_grade())
    print(lisa.age)
