#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器
# 不断推算出后续的元素
# generator保存的是算法
# StopIteration

gg = (x * x for x in range(1, 11))
print(gg)
# print(next(gg))

for g in gg:
    print(g)


# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行
def fib_with_yield(max):
    if max <= 0:
        return None
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # yield关键字会将一个函数变为生成器
        a, b = b, a + b
        n += 1
    return "Done"


def fib(max):
    if max <= 0:
        return None
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n += 1
    return a


print("fib-10:", fib(10))
for fib in fib_with_yield(10):
    print(fib)


def triangles():
    ll = [1]
    while 1:
        yield ll
        ll = [1] + [ll[j] + ll[j + 1] for j in range(len(ll) - 1)] + [1]


triangles = triangles()
print(next(triangles))
print(next(triangles))
print(next(triangles))
print(next(triangles))
