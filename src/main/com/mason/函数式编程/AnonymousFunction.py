#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 冒号前是输入，后面是匿名函数的返回值
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ll = list(map(lambda x: x * x, ll))
print(ll)

# 虽然lambda匿名表达式可以赋值给变量进行调用
# 但是并不推荐这么用
ff = lambda x: x ** 2
ll = list(map(ff, ll))
print(ll)


# 匿名函数也可以作为返回值
def build(x, y):
    return lambda: x * x + y * y


print(build(1, 2))
print(build(1, 2)())

ll = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(ll)
