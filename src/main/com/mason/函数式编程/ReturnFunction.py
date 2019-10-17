#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回


def calc_sum(*nums):
    result = 0
    for num in nums:
        result += num
    return result


print(calc_sum(1, 2, 3))


# 在这个例子中，我们在函数lazy_sum中又定义了函数sum
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

def lazy_sum(*nums):
    def sum():
        result = 0
        for num in nums:
            result += num
        return result

    return sum


lazy = lazy_sum(1, 2, 3)
print(lazy)
print(lazy())


# 闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        return lambda: j ** 2

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def create_counter():
    result = 0

    def counter():
        nonlocal result
        result += 1
        return result

    return counter


counter = create_counter()
print(counter())
print(counter())
print(counter())
print(counter())
