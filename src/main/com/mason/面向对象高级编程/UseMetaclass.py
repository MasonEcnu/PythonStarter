#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的


def fn(self, name="world"):
    print("Hello %s" % name)


# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 创建Hello Class
# 要创建一个class对象，type()函数依次传入3个参数：
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type("Hello", (object,), dict(hello=fn))
h = Hello()
h.hello()

print(type(h))
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法
# 然后调用type()函数创建出class

# 元类--metaclass
