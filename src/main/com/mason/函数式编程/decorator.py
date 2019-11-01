#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器
# 本质上，decorator就是一个返回函数的高阶函数
import functools
import time


def log(func):
    def wrapper(*args, **kwargs):
        print("call %s()" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


# log接收参数
# now = log('execute')(now)
# 首先执行log('execute')，返回的是decorator函数
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数
def log_text(text):
    def decorator(func):
        # 把原始函数的__name__等属性复制到wrapper()函数中
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 等价于now = log(now)
@log_text("execute")
def now():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


now()
# 此时调用now，实际上是调用log_text中的wrapper函数
print(now.__name__)


# 打印函数的执行时间
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print('%s executed in %d ms' % (fn.__name__, end - start))

    return wrapper


@metric
def sleep():
    time.sleep(1.0)


sleep()
