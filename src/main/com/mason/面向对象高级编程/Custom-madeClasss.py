#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定制类


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Student(name:%s, age:%d)" % (self.name, self.age)

    __repr__ = __str__

    # 只有在没有找到属性的情况下
    def __getattr__(self, item):
        if item == "score":
            return 100
        if item == "rank":
            return lambda x: x + 10


stu = Student("Mason", 22)
print(stu)
print(stu.score)
print(stu.rank(10))


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        if isinstance(item, int):
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            if start is None:
                start = 0
            if stop is None:
                stop = start + 10

            result = []
            for x in range(stop):
                if x >= start:
                    start += step
                    result.append(a)
                a, b = b, a + b
            return result


# for n in Fib():
#     print(n)

print(Fib()[1:10:1])
print(Fib()[1:10:2])


# rest full
class Chain(object):
    def __init__(self, path=""):
        self.path = path

    def __getattr__(self, path):
        if path == "users":
            return lambda x: Chain("%s/users/%s" % (self.path, x))
        return Chain("%s/%s" % (self.path, path))

    def __str__(self):
        return self.path

    # 像调用方法一样，调用类的实例
    def __call__(self, *args, **kwargs):
        print("path: %s" % self.path)


chain = Chain("root")
print(chain.status.user.list)
print(chain.users("mason").user.list)
chain()

# callable:判断一个类的实例是否可调用
print(callable(chain))
