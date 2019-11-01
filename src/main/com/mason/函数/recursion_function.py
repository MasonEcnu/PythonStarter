#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归函数


# 阶乘
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(10))


# 尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def fact_new(num):
    return fact_iter(num, 1)


print(fact_new(10))


# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')
