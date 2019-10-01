#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断
age = 22
if age >= 18:
    print("You are a adult.")
else:
    print("You are too young.")

age = 10
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("child")

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = None
if x:
    print(True)

weight = float(input("请输入你的体重："))
height = float(input("请输入你的身高："))
bmi = weight / (height * height)
print("bmi:%f" % bmi)
if bmi >= 32:
    print("严重肥胖")
elif bmi >= 28:
    print("肥胖")
elif bmi >= 25:
    print("过重")
elif bmi >= 18.5:
    print("正常")
else:
    print("过轻")
