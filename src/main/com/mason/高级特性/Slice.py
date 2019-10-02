#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 去前三个元素
# [)：半开半闭区间
print(L[0:3])
print(L[:3])

# 从后往前是从-1开始
# []：全闭区间
print(L[-2:])

L = list(range(100))
# 第三个参数是步长
print(L[-20:-10:2])


# 利用切片实现trim函数，即就是strip
def trim(s: str):
    if len(s) <= 0:
        return s
    start = 0
    end = len(s)

    for c in s:
        if c != " ":
            break
        start += 1

    for c in s[::-1]:
        if c != " ":
            break
        end -= 1

    if start <= end:
        return s[start:end]
    return ""


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
