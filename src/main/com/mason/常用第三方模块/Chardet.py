#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# chardet
import chardet

print(chardet.detect(b"Hello World!"))

data = "离离原上草，一岁一枯荣".encode("gbk")
print(chardet.detect(data))
data = "离离原上草，一岁一枯荣".encode("utf-8")
print(chardet.detect(data))
