#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件读写
# 文件使用完毕后必须关闭


file_path = r"D:\PyCode\PythonStarter\src\main\resources\io_test.txt"


def test_file_read():
    try:
        file = open(file_path, "r")
        # n:读取文件的长度
        print(file.read(10))

    except FileNotFoundError as err:
        print(err)
    except IOError as err:
        print(err)
    finally:
        if file:
            file.close()


def test_file():
    # with:自动释放资源
    # file.close()
    with open(file_path, "r") as file:
        print(file.read())


def test_file_read_line():
    # with:自动释放资源
    # file.close()
    with open(file_path, "r") as file:
        file_line = file.readline()
        while file_line:
            print(file_line)
            file_line = file.readline()


# if __name__ == '__main__':
#     test_file_read_line()

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object

# 二进制文件
# b-->二进制
open(file_path, mode="rb")

# 字符编码
# 二进制模式下，不需要指定encoding
# errors:ignore遇到错误时，忽略
open(file_path, mode="r", encoding="utf-8", errors="ignore")


# 写文件
# 关于open()的mode参数：
# r’：读
# w’：写
# a’：追加
# r+’ == r+w（可读可写，文件若不存在就报错(IOError)）
# w+’ == w+r（可读可写，文件若不存在就创建）
# a+’ ==a+r（可追加可写，文件若不存在就创建）
def test_file_write():
    # mode="w"-->直接覆盖内容
    # mode="wa"-->直接覆盖内容
    with open(file_path, mode="a") as file:
        if file.writable():
            file.write("\nHello World!")


if __name__ == '__main__':
    test_file_write()
