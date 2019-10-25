#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多线程--multithreading
# Posix Thread
import multiprocessing
import threading
import time


def loop():
    print("Loop Thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("Thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("Loop Thread %s end..." % threading.current_thread().name)


def test_thread():
    print("Test_thread %s is running..." % threading.current_thread().name)
    thread = threading.Thread(target=loop, name="LoopThread")
    thread.start()
    thread.join()
    print("Test_thread %s end..." % threading.current_thread().name)


# if __name__ == '__main__':
#     test_thread()


# lock
balance = 0
lock = threading.Lock()


def change_balance(n):
    global balance
    balance += n
    balance -= n


def run_change_balance(n):
    for i in range(10000000):
        # 获取锁
        lock.acquire()
        try:
            change_balance(n)
        finally:
            # 释放锁
            lock.release()


def test_change_balance():
    t1 = threading.Thread(target=run_change_balance, args=(11,))
    t2 = threading.Thread(target=run_change_balance, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


# if __name__ == '__main__':
#     test_change_balance()

def dead_loop():
    x = 0
    while True:
        x = x ^ 1


# GIL锁：Global Interpreter Lock
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=dead_loop)
    t.start()
