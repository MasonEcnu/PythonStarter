#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取对象信息

# 使用type()
# type==对应的Class类型
import types

from src.main.com.mason.面向对象编程.InheritAndPolymorphism import Dog, Cat, Animal

print(type(123))
print(type("123"))
print(type(None))
print(type(abs))


def test():
    pass


# 使用isinstance()
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”

dog = Dog()
cat = Cat()

if __name__ == '__main__':
    print(type(test) == types.FunctionType)
    print(isinstance(test, types.FunctionType))
    print(isinstance(dog, Animal))
    print(isinstance([1, 2, 3], (list, tuple)))

# 使用dir()
# 获取对象的所有属性和方法

if __name__ == '__main__':
    print(dir(dog))
    print(len(dog))
    print(len(cat))

    print(getattr(dog, "hash", "hash属性/方法不存在"))
    print(hasattr(dog, "eat"))
