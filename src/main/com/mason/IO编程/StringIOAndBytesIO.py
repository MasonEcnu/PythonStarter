#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# StringIO和BytesIO


# StringIO
# 内存中读写str
from io import StringIO, BytesIO


def test_string_io_write():
    sio = StringIO()
    sio.write("Hello")
    sio.write(" ")
    sio.write("World!")
    print(sio.getvalue())
    sio.close()


def test_string_io_read():
    sio = StringIO("\nHello\nHi\nWorld!")
    sio.write("123\n")
    print(sio.getvalue())
    print("--------------------")
    while True:
        content = sio.readline()
        if not content:
            break
        # strip-->trim
        print(content.strip())
    sio.close()


if __name__ == '__main__':
    test_string_io_write()
    test_string_io_read()


# BytesIO
# 处理二进制数据
def test_bytes_io_read():
    bio = BytesIO(b"\xe4\xb8\xad\xe6\x96\x87")
    print(bio.read())
    bio.close()


def test_bytes_io_write():
    bio = BytesIO()
    bio.write("中文".encode("utf-8"))
    print(bio.getvalue())
    bio.close()


if __name__ == '__main__':
    test_bytes_io_read()
    test_bytes_io_write()
