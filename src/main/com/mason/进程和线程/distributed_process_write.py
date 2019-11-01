#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 分布式进程
# 分布式多进程程序
# 写进程

import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()


def get_task_queue():
    return task_queue


# 接收结果的队列
result_queue = queue.Queue()


def get_result_queue():
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 把两个Queue都注册到网络上，callable参数关联Queue对象
    QueueManager.register("get_task_queue", callable=get_task_queue)
    QueueManager.register("get_result_queue", callable=get_result_queue)
    # 绑定5000端口，设置验证码为abc
    server_addr = '127.0.0.1'
    manager = QueueManager(address=(server_addr, 5000), authkey=b"abc")
    # 启动
    manager.start()
    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print("Put task %d....." % n)
        task.put(n)

    # 从result读取结果
    print("Try get results......")
    for i in range(10):
        r = result.get(timeout=100)
        print("Result: %s" % r)

    # 关闭
    manager.shutdown()
    print("Manager exit......")
