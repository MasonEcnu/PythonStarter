#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数的参数
# 默认参数、可变参数和关键字参数
# 一是必选参数在前，默认参数在后
# 默认参数必须指向不变对象


def power(x, n=2):
    result = 1
    for i in range(n):
        result *= x
    return result


print(power(12, 3))


# 可变参数
# list或tuple
def sum_power(*numbers, n=2):
    sum = 0
    for num in numbers:
        sum += power(num, n)
    return sum


# *numbers表示把numbers这个list的所有元素作为可变参数传进去
numbers = [1, 2, 3]
print(sum_power(*numbers, n=3))


# 关键字参数
# 关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("mason", 11)
person("mason", 11, **extra)


# 命名关键字参数
# *分割，带命名的关键字，调用时必填
def person(name, age, *, city, job):
    print("name:", name, "age:", age, "city:", city, "job:", job)


person("mason", 11, city="shanghai", job="software engineer")


def person(name, age, *args, city, job):
    print("name:", name, "age:", age, "city:", city, "job:", job, "other:", args)


# list转为了tuple
person("mason", 11, [1, 2, 3], city="shanghai", job="software engineer")


# 参数组合
# 顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kwargs):
    print("a=", a, "b=", b, "c=", c, "args=", args, "kwargs=", kwargs)


def f2(a, b, c=0, *, d, **kwargs):
    print("a=", a, "b=", b, "c=", c, "d=", d, "kwargs=", kwargs)


f1(1, 2)

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


def product(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试成功!')
    except TypeError:
        print('测试失败!')
