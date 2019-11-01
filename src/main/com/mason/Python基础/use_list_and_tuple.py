#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list--[]
# 有序集合
# 随机访问
# python没有泛型

print("----------list----------")
random_num = [2, 1, 3, 5, 2]
len(random_num)
print(random_num[1])
print(random_num[-1])  # 负号表示从后往前
# IndexError: list index out of range
random_num.append("a")  # 追加元素到末尾
random_num.insert(2, "b")  # 追加元素到指定index
print(random_num)
random_num.pop()  # 弹出末尾元素
random_num.pop(3)  # 删除指定位置元素
random_num[2] = 11
print(random_num)

# tuple--()
# tuple一旦初始化就不能修改
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
# 但，如果tuple中的元素有list，则该list中的元素是可变的
print("----------tuple----------")
t = ()
print(len(t))
t = (1,)  # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
print(t)
