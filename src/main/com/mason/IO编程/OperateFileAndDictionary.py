#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 操作文件和目录
import os

print(os.name)


# os.uname()--windows系统下不提供
# print(os.uname())


# 环境变量
def test_system_env():
    for k, v in os.environ.items():
        print("%s:%s" % (k, v))


# if __name__ == '__main__':
#     test_system_env()


# 操作文件和目录
def test_system_file_dir():
    # 获取绝对路径
    abs_path = os.path.abspath(".")
    # 创建新的目录
    new_path = os.path.join(abs_path, "new_dir")
    if os.path.exists(new_path):
        os.rmdir(new_path)
    os.mkdir(new_path)

    # os.path.split()--获取文件名+扩展
    # os.path.splitext()--获取扩展名
    # os.rename()--重命名
    # os.remove()--删除文件
    # os.path.isdir()--是否目录
    # os.path.isfile()--是否文件


# if __name__ == '__main__':
#     test_system_file_dir()


# 练习
# 1.利用os模块编写一个能实现dir -l输出的程序
def test_dir_list(path):
    if not isinstance(path, str):
        raise ValueError("输出路径必须是string类型: %s" % path)
    for l in [x for x in os.listdir(path)]:
        print(l)


# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def test_query_file_by_name(base_path, name):
    if not base_path:
        base_path = "."
    if not isinstance(base_path, str):
        raise ValueError("输出路径必须是string类型: %s" % base_path)
    if not os.path.exists(base_path):
        raise ValueError("路径不存在: %s" % base_path)

    for x_path in [x for x in os.listdir(base_path)]:
        file_path = os.path.join(base_path, x_path)
        if os.path.isdir(file_path):
            test_query_file_by_name(file_path, name)
        elif os.path.isfile(file_path) and name in x_path.split(",")[0]:
            print(file_path)


if __name__ == '__main__':
    path = r"C:\Users\mwu\Desktop\技术书籍"
    # test_dir_list(path)

    test_query_file_by_name(path, name="Java")
