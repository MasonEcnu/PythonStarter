#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 过滤器--filter
# filter()函数返回的是一个Iterator
from math import sqrt


def is_odd(n):
    return n % 2 == 1


ll = list(range(1, 11))
result = list(filter(is_odd, ll))
print(result)

ll = list(range(1, 1001))


def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    sq = int(sqrt(n))
    for i in range(2, sq + 1):
        if n % i == 0:
            return False
    return True


result = list(filter(is_prime, ll))
print(result)
print(len(result))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


# 素数生成器
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 回文数
def is_palindrome(n):
    index = 0
    ss = str(n)
    total_len = len(ss)
    half_len = int(total_len / 2)
    while index < half_len:
        if ss[index] != ss[total_len - index - 1]:
            return False
        index += 1

    return True


ll = list(range(1, 1001))
result = list(filter(is_palindrome, ll))
print(result)
