#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 继承和多态
# Python的“file-like object“就是一种鸭子类型
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的


class Animal(object):
    def run(self):
        print("Animal is running......")

    def eat(self):
        print("Animal is eating......")


class Dog(Animal):

    def run(self):
        print("Dog is running......")

    def eat(self):
        print("Dog is eating......")


class Cat(Animal):
    def run(self):
        print("Cat is running......")

    def eat(self):
        print("Cat is eating......")


if __name__ == "__main__":
    cat = Cat()
    cat.run()
    cat.eat()
