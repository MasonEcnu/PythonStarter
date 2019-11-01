#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承
# 通过多重继承来组合多个MixIn的功能


# 动物基类
class Animal(object):
    pass


# 哺乳类动物
class Mammal(Animal):
    pass


# 鸟类
class Bird(Animal):
    pass


# 会跑的动物
class Runnable(object):
    def run(self):
        print("running......")


# 会飞的动物
class Flyable(object):
    def fly(self):
        print("flying......")


# 各类动物
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Runnable):
    pass


dog = Dog()
dog.run()
parrot = Parrot()
parrot.fly()
