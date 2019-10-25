#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正则表达式是一种用来匹配字符串的强有力的武器
# 如果直接给出字符，就是精确匹配

# \d可以匹配一个数字，\w可以匹配一个字母或数字
# .可以匹配任意字符
# 用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符

# 进阶
# 要做更精确地匹配，可以用[]表示范围，比如：
# 1.0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
# 2.[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如"a100"，"0_Z"，"Py3000"等等；
# 3.[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
# 4.[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
#
# A|B可以匹配A或B，所以(P|p)ython可以匹配"Python"或者"python"。
#
# ^表示行的开头，^\d表示必须以数字开头。
#
# $表示行的结束，\d$表示必须以数字结束。
#
# 你可能注意到了，py也可以匹配"python"，但是加上^py$就变成了整行匹配，就只能匹配"py"了。
import re

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
re_match = re.match(r"^\d{3}\-\d{3,8}$", "010-1234511111")
if re_match:
    print(re_match.group())
else:
    print("not match")

# 切分字符串
re_split = re.split(r"\s+", "a  b c  ".strip())
print(re_split)

re_split = re.split(r"[\s+\,\;]+", "a   d,c  b c d;f  ".strip())
print(re_split)

# 分组
date = "12:23:00"
re_match = re.match(
    r"^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:"
    r"(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$",
    date)

if re_match:
    print(re_match.group())
else:
    print("not match")

# 贪婪匹配
# 正则匹配默认是贪婪匹配--匹配尽可能多的字符
re_match = re.match(r'^(\d+)(0*)$', '102300')
print(re_match.groups())

# 非贪婪
re_match = re.match(r'^(\d+?)(0*)$', '102300')
print(re_match.groups())

# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2.用编译后的正则表达式去匹配字符串。

# 预编译
re_telephone = re.compile(r"^(\d{3})-(\d{3,8})$")
re_match = re_telephone.match("010-12345")
print(re_match.groups())

email_re = re.compile(r"^[1-9a-zA-Z][0-9a-zA-Z\_\.\-]*@([a-z]+?)\.(com|cn|org)")


def is_valid_email(addr):
    m = email_re.match(addr)
    return m is not None


# print(is_valid_email("123._abc123@qq.com"))
# print(is_valid_email("someone@gmail.com"))
# print(is_valid_email("bill.gates@microsoft.com"))
# print(is_valid_email("bob#example.com"))
# print(is_valid_email("mr-bob@example.com"))
# print(is_valid_email("tom@voyager.org"))

email_name_re = re.compile(r"<?([a-zA-Z]+\s?[a-zA-Z]*)>?[\w\s]*")
"(^[1-9a-zA-Z][0-9a-zA-Z\_\.\-]*@([a-z]+?)\.(com|cn|org))"


def name_of_email(addr):
    m = email_name_re.match(addr)
    if m:
        return m.group(1)
    else:
        return None


print(name_of_email("<TomParis> tom@voyager.org"))
print(name_of_email("tom@voyager.org"))
