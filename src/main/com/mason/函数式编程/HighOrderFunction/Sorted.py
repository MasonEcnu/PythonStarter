#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

# sorted 排序算法
# 默认升序
from src.main.com.mason.工具 import random_list

ll = random_list(10)
print("排序前：", ll)
ll = sorted(ll)
print("排序后：", ll)

# 指定key函数的话，sorted会对ll根据key的计算结果排序
sorted(ll, key=abs)

ll = ['bob', 'about', 'Zoo', 'Credit']
ll = sorted(ll)
# 字符串默认是按ASCII，升序排列
print("排序后：", ll)
# 忽略大小写
ll = sorted(ll, key=str.lower)
print("排序后-忽略大小写：", ll)
# 反向
ll = sorted(ll, key=str.lower, reverse=True)
print("排序后-忽略大小写-反向：", ll)

mm = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


mm = sorted(mm, key=lambda t: t[0])
print("排序后：", mm)
mm = sorted(mm, key=lambda t: t[1])
print("排序后：", mm)
mm = sorted(mm, key=by_score)
print("排序后：", mm)
# itemgetter 用于获取对象的哪些位置的数据，参数即为代表位置的序号值
mm = sorted(mm, key=itemgetter(0))
print("排序后：", mm)
