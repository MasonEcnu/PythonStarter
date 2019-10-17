#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用模块

# 任何模块代码的第一个字符串都被视为模块的文档注释
"a test module"

__author__ = "Mason"

import sys


# 运行python3 hello.py获得的sys.argv就是['hello.py']；
# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
# sys.argv的第一个参数永远是文件名，全路径的
def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print("Hello World!")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")


# 用于测试
# 保证别的模块在引入该模块时
# 不会执行代码
if __name__ == "__main__":
    test()

# 作用域
# 类似__xxx__这样的变量是特殊变量
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private）
