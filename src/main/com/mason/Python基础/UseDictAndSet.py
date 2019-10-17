#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用dict和set

# dict：字典--{}
# dict的key必须是不可变对象
score_map = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(score_map)
score_map["Mason"] = 111  # 新增
score_map.popitem()  # 弹出最后一个
for name, score in score_map.items():
    print("%s--%d" % (name, score))

# set--{}
# key不可重复
s = {1, 2, 3, 1}
s.add(4)
print(s)
s.pop()
s.remove(3)
# TypeError: unhashable type: 'list'
s = {1, 2, 3, [1, 2, 3]}
print(s)
