#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Hello World!")

age = input("请输入你的年龄：")
if age.isnumeric():
    print("年龄:", age)
else:
    print("输入错误，请输入数字！")
