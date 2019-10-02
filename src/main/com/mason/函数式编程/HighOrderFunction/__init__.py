#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数

# 变量可以指向函数

# built-in function abs：内建函数
print(abs)

# 函数本身也可以赋值给变量，即：变量可以指向函数
v_abs = abs

print(v_abs(-10))


# 函数名也是变量
# 函数名其实就是指向函数的变量

# 传入函数
# 可以接收函数作为参数的函数，成为高阶函数

def add_power(x, y, power):
    return power(x) + power(y)


def power(x):
    return x ** 2


print(add_power(2, 3, power))
