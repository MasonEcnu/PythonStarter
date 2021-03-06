#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据结构和变量

# 整数
a = 1
a = 100
a = 0
a = 0xff00  # 十六进制

# 浮点数
b = 1.23
b = -2.3
b = 1.23e5  # 科学计数法e=10

# 字符串
s = "abc"
s = "a"
s = "I'm a boy"
s = "I said: \"OK\""  # 反斜杠转义

"\n" "\t"  # 换行符，制表符

s = r"\\\t\\"  # r表示默认不转义
s = """
a
b
c
"""  # """..."""：多行字符串

# 布尔值
f = True
f = False
f = a > b
f = a and b
f = a or b
f = not a

# 空值
None

# 变量
# 以上:a、b、s、f都称为变量
# a = 'ABC'
# Python解释器干了两件事情：
# 1.在内存中创建了一个'ABC'的字符串；
# 2.在内存中创建了一个名为a的变量，并把它指向'ABC'。

# 常量
# 通常用全大写表示，连接符号为_下划线
PI = 3.1415926

# 运算符
# 除法
10 / 3  # 3.333333
9 / 3  # 3.0
# 单个/符号的除法，结果为浮点数

# 地板除法--结果为整数
10 // 3  # 3

# 取余
10 % 3  # 1

# Python的整数没有大小限制
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
