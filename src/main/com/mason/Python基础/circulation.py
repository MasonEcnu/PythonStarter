#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环

names = ["Michael", "Bob", "Tracy"]
for name in names:
    print(name)

sum = 0
# range(n) = 0,1,2,...,n-1
for i in range(101):
    sum += i
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

sum = 0
n = 100
while n > 0:
    sum += n
    if sum > 1000:
        break
    n -= 2
print(sum)

# continue:跳过本次循环，继续下一次
