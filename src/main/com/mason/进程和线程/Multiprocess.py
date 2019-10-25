#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多进程--multiprocessing
import os
import random
import subprocess
import time
from multiprocessing import Process, Pool, cpu_count, Queue


def test_process_in_unix():
    print("Process (%s) start......" % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print("I am child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))
    else:
        print("I (%s) just created a child process (%s)." % (os.getpid(), pid))


def run_proc(name):
    print("Run child process %s (%s)" % (name, os.getpid()))


def test_process_in_windows():
    print("Parent process %s" % os.getpid())
    p = Process(target=run_proc, args=("test",))
    print("Child process will start......")
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print("Child process end......")


# if __name__ == '__main__':
#     test_process_in_windows()

# poll--进程池
def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %.2f seconds." % (name, (end - start)))


def test_process_pool_in_windows():
    print("Parent process %s." % os.getpid())
    cc = cpu_count()
    proc_pool = Pool(cc)
    for i in range(cc + 1):
        proc_pool.apply_async(long_time_task, args=(i,))
    print("Waiting for all subprocesses done......")
    proc_pool.close()
    proc_pool.join()
    print("All subprocesses done.")


# todo 代码执行无法结束了。。。
# if __name__ == '__main__':
#     test_process_pool_in_windows()


# 子进程
# 貌似在windows上无法正常执行
def test_subprocess_in_windows():
    print("$ nslookup www.python.org")
    r = subprocess.call(["nslookup", "www.python.org"])
    print("Exit code: %s" % r)


def test_subprocess_input():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


# if __name__ == '__main__':
#     test_subprocess_input()

# 进程间通信
# Queue和Pipes

def write_to_process(queue):
    print("Process to write: %s" % os.getpid())
    for value in ["A", "B", "C"]:
        print("Put %s to queue..." % value)
        queue.put(value)
        time.sleep(random.random())


def read_from_process(queue):
    print("Process to read: %s" % os.getpid())
    while True:
        value = queue.get(True)
        print("Get %s from queue." % value)


def test_inter_process_communication():
    queue = Queue()
    proc_write = Process(target=write_to_process, args=(queue,))
    proc_read = Process(target=read_from_process, args=(queue,))
    # 启动写入进程
    proc_write.start()
    # 启动读进程
    proc_read.start()
    # 等待执行结束
    proc_write.join()
    # 读进程里是死循环
    proc_read.terminate()


# PermissionError: [WinError 5] 拒绝访问。
if __name__ == '__main__':
    test_inter_process_communication()
