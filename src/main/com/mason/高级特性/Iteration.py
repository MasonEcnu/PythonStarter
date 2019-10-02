#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterable

# 迭代
# 迭代是通过for ... in来完成的
from src.main.com.mason.工具 import random_list

print(isinstance("str", Iterable))

ll = random_list(10)
for index, value in enumerate(ll):
    print("index:", index, "value:", value)


def find_min_and_max(L):
    if len(L) <= 0:
        return None, None
    min = L[0]
    max = L[0]

    for x in L:
        if x < min:
            min = x

        if x > max:
            max = x
    return min, max


ll = random_list(0)
print(ll)
print(find_min_and_max(ll))
