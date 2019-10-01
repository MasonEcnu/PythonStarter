#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数的参数
# 默认参数、可变参数和关键字参数
# 一是必选参数在前，默认参数在后
# 默认参数必须指向不变对象


def power(x, n=2):
    result = 1
    for i in range(n):
        result *= x
    return result


print(power(12, 3))

# 可变参数
