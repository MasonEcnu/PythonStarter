#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 偏函数

# int默认是十进制
import functools

num = int("12", base=8)
print(num)

# 等价于
# def int2(num, base=2):
#     return int(num, base)
# kw = { 'base': 2 }
# int('10010', **kw)
int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int2("10"))
print(int8("10"))
print(int16("10"))

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
