#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代器--Iterator
# 可迭代对象：Iterable
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 这是因为Python的Iterator对象表示的是一个数据流
# Iterator的计算是惰性的

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列

print(iter("123"))
print(iter([1, 2, 3]))

for x in [1, 2, 3, 4, 5]:
    pass

# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
