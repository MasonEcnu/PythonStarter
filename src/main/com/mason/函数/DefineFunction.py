#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


# from abstest import my_abs
# from package import function
# 定义函数
# 函数默认返回None


def my_abs(n):
    if not isinstance(n, (int, float)):
        raise TypeError("bad operand type")
    if n >= 0:
        return n
    else:
        return -n


my_abs_test = my_abs
print(my_abs_test(-1))


# 空函数
# pass

def empty_func():
    pass


def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 返回多个值
# 其实返回结果就是个tuple
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# ax2+bx+c=0 的两个解
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("bad operand type:" + a)
    if not isinstance(b, (int, float)):
        raise TypeError("bad operand type:" + b)
    if not isinstance(c, (int, float)):
        raise TypeError("bad operand type:" + c)

    temp = b ** 2 - 4 * a * c
    if temp < 0:
        return "no solution"

    if temp == 0:
        return - b / 2

    x = (-b + math.sqrt(temp)) / (2 * a)
    y = (-b - math.sqrt(temp)) / (2 * a)
    return x, y


print(quadratic(3, 6, 3))
