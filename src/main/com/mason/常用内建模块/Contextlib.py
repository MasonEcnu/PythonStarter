#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# contextlib
# 任何对象，只要正确实现了上下文管理，就可以用于with语句
from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Begin:")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error")
        else:
            print("End")

    def query(self):
        print("Query info about %s" % self.name)


with Query("Bob") as q:
    q.query()


# @contextmanager
# 更简单的写法
class NewQuery(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print("Query info about %s" % self.name)


@contextmanager
def create_query(name):
    print("Begin:")
    yield NewQuery(name)
    print("end!")


with create_query("Mason") as q:
    q.query()


# 某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    # 这里可以包装成一个方法
    print("hello")
    print("world")

# 代码的执行顺序是：
# 1.with语句首先执行yield之前的语句，因此打印出<h1>；
# 2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3.最后执行yield之后的语句，打印出</h1>。

# @closing
# 用closing()来把该对象变为上下文对象
with closing(urlopen("https://www.python.org")) as page:
    for line in page:
        print(line)


# 如果thing，没有实现close方法呢？
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
