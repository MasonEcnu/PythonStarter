#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 列表生成器
# List Comprehensions
list(range(1, 11))

# 列表生成式
ll = [x * x for x in range(1, 11) if x % 2 == 0]
print(ll)
# 生成全排列
ll = [m + n for m in 'ABC' for n in 'XYZ']
print(ll)
ll = [d for d in os.listdir(".")]
print(ll)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
ll = [k + "=" + v for k, v in d.items()]
print(ll)

ll = ['Hello', 'World', 12, 'IBM', 33, 'Apple']

ll = [s.lower() for s in ll if isinstance(s, str)]
print(ll)
