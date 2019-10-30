#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# psutil
# psutil = process and system utilities
import psutil

# 4核心8线程
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

# 统计cpu时间
print(psutil.cpu_times())

# 类似top命令
for i in range(5):
    print(psutil.cpu_percent(interval=.1, percpu=True))

# 获取内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘信息
# 磁盘分区
print(psutil.disk_partitions())
# 磁盘使用
print(psutil.disk_usage("/"))
# 磁盘IO
print(psutil.disk_io_counters())

# 获取网络信息
# 获取网络读写字节／包的个数
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())
# 获取网络连接信息
print(psutil.net_connections())

# 获取进程信息
# 所有进程id
print(psutil.pids())
p = psutil.Process(10408)
# 进程名称
print(p.name())
# 进程exe路径
print(p.exe())
# 进程工作路径
print(p.cwd())
# 进程启动命令行
print(p.cmdline())
# 父进程id
print(p.ppid())
print(p.parent())
print(p.children())
# 进程状态
print(p.status())
# 进程用户名
print(p.username())
# 进程创建时间--时间戳
print(p.create_time())
print(p.cpu_times())
print(p.memory_info())
print(p.open_files())
print(p.connections())
# 进程的线程数量
print(p.num_threads())
print(p.threads())
print(p.environ())
# print(p.terminate())


# 模拟ps命令
print(psutil.test())
