#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# struct
# 准确地讲，Python没有专门处理字节的数据类型。
# 但由于b"str"可以表示字节，所以，字节数组＝二进制str

# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
import base64
import struct

# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# int转bytes
print(struct.pack(">I", 10240099))

# bytes转其他
# >IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
print(struct.unpack(">IH", b"\xf0\xf0\xf0\xf0\x80\x80"))

# 读入前30个字节
s = b"\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00" \
    b"\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00"

print(struct.unpack('<ccIIIIIIHH', s))

# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小； 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量； 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
bmp_data = base64.b64decode(
    "Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3"
    "//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9"
    "//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8"
    "/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9"
    "//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3"
    "//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f"
    "/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9"
    "/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz"
    "/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==")


def bmp_info(data: bytes):
    data = data[:30]
    # 判断是否位图
    ds = struct.unpack('<ccIIIIIIHH', data)
    if not ds:
        raise ValueError("不是位图:", ds)
    f_ds = ds[0] + ds[1]
    if not (f_ds == b"BM" or f_ds == b"BA"):
        raise ValueError("不是位图:", f_ds)
    return {
        'width': ds[6],
        'height': ds[7],
        'color': ds[9]
    }


bi = bmp_info(bmp_data)
print(bi)
