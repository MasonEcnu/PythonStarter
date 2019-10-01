#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# UTF-8 without BOM
# 字符串和编码
# 在计算机内存中，统一使用Unicode编码

# 字符编码
# ASCII:1字节
# Unicode:通常2字节
# Utf-8:可变长编码--1-6个字节
# 英文字母1字节，汉字通常3字节

# 字符串
# 最新的Python 3版本中，字符串是以Unicode编码的

# 字符转整数
ni = ord("你")
print(ni)
# 整数转字符
ni = chr(ni)
print(ni)

s = "\u4e2d\u6587"
print(s)

# 转码
b"abc"  # 表示"abc"的bytes格式
bs = "ABC不是中文".encode("utf-8")
print(bs)
bs = bs.decode("utf-8")
print(bs)

# 如果bytes里包含编码格式无法解码的字符
# UnicodeDecodeError
# errors='ignore'：传入这个参数，可以部分解码
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

print(len(bs))

# 格式化
print("Age:%d %%, Gender:%s" % (11, True))
print("%2d-%02d" % (3, 1))
print("%.2f" % 3.1475926)  # 四舍五入

ss = "Hello, {0}, 成绩提升了 {1:.1f}%".format("Mason", 15.25)  # 这里不会四舍五入
print(ss)
