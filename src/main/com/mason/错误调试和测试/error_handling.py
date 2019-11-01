#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


# 错误处理


def foo():
    r = int(input("请输入一个数："))
    if r == -1:
        return -1
    # do something
    return r


def bar():
    r = foo()
    if r == -1:
        print('Error')
    else:
        pass


# bar()

# try
import logging


def test_try():
    a, b = input("输入a="), input("输入b=")
    if a.lower() == "exit":
        print("exit......")
        exit(0)
    try:
        print("trying......")
        r = int(a) / int(b)
        print("result=%.2f" % r)
    except ZeroDivisionError as err:
        logging.exception(err)
        print("error: %s" % err)
    except ValueError as err:
        logging.exception(err)
        print("error: %s" % err)
    else:
        print("no error......")
    finally:
        print("finally......")


# while True:
#     test_try()

# 调用栈
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置
# 调用栈==出错时的堆栈信息


# 抛出错误
# raise
# raise语句如果不带参数，就会把当前错误原样抛出

# 练习
def str2num(s):
    if "." in s:
        return float(s)
    return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
