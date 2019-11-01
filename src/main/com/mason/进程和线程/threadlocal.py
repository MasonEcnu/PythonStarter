#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ThreadLocal
import threading

local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print("Hello %s (in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


def test_process_thread():
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    test_process_thread()
