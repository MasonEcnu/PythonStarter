#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# base64
# Base64是一种用64个字符来表示任意二进制数据的方法
# Base64是一种通过查表的编码方法
import base64

b64_encode = base64.b64encode(b"binary\x00string")
print(b64_encode)
b64_decode = base64.b64decode(b64_encode)
print(b64_decode)

# url-safe
print("------------url-safe------------")
b64_encode = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b64_encode)
b64_url_safe_encode = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b64_url_safe_encode)
b64_url_safe_decode = base64.urlsafe_b64decode(b64_url_safe_encode)
print(b64_url_safe_decode)


# 写一个能处理去掉=的base64解码函数
# Base64编码的长度永远是4的倍数
def safe_base64_decode(s):
    diff_len = 4 - len(s) % 4 if len(s) % 4 > 0 else 0
    s = s + b"=" * diff_len
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print("ok")
