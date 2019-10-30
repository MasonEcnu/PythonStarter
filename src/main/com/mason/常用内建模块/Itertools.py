#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# itertools

# 无限迭代器
# repeat()
import itertools

naturals = itertools.count(1)
for n in naturals:
    if n > 100:
        break
    print(n)

cs = itertools.cycle("ABC")
count = 0
for c in cs:
    if count > 100:
        break
    print(c)
    count += 1

ns = itertools.takewhile(lambda x: x <= 10, itertools.count(1))
print(list(ns))

# chain()
# 把一组迭代对象串联起来，形成一个更大的迭代器
print(list(itertools.chain("123", "abc")))

# groupby()
# 把迭代器中相邻的重复元素挑出来放在一起
# key:value(list)
# lambda x: x.upper():分组条件
print(list(itertools.groupby("aabbsscc", lambda x: x.upper())))


# 练习
# 计算圆周率
def pi(N):
    """
    计算pi的值
    :param N:
    :return:
    """
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_iter = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_list = list(itertools.takewhile(lambda x: x <= 2 * N - 1, odd_iter))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in range(len(odd_list)):
        if i % 2 == 1:
            odd_list[i] = -odd_list[i]
        odd_list[i] = 4 / odd_list[i]
    # step 4: 求和:

    # p, c = 0, 1
    # for si in odd_list:
    #     p, c = p + c * 4 / si, -c
    # return p

    return sum(odd_list)


assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
