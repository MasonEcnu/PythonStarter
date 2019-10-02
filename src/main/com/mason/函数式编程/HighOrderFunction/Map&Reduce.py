#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map
# map(function, iter)
# 将func作用于iter的每一个元素上
# 并生成一个新的iter返回--Iterator
from functools import reduce

ll = list(range(1, 11))


def power(x):
    return x ** 2


def add(x, y):
    return x + y


result = list(map(power, ll))
print(result)

result = list(map(str, result))
print(result)

# reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算
# 求和

print(ll)
result = reduce(add, ll)
print(result)


def fn(x, y):
    return x * 10 + y


result = reduce(fn, ll)
print(result)

# 字符串转数字
DIGITS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


def char_to_num(s):
    return DIGITS[s]


def str_to_int(s):
    return reduce(lambda x, y: x * 10 + y, map(char_to_num, s))


print(str_to_int("123"))

in_list = ["adam", "LISA", "barT"]


def capitalize(s: str):
    return s.capitalize()


out_list = list(map(capitalize, in_list))
print(out_list)


# 求list的积
def prod(ll):
    return reduce(lambda x, y: x * y, ll)


print(prod(ll))


# 字符串转浮点数
def str_to_float(s: str):
    dot = s.find(".")
    temp = s.replace(".", "")
    return str_to_int(temp) / (10 ** (len(temp) - dot))


print(str_to_float("123.45"))
