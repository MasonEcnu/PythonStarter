#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 海龟绘图

# 导入turtle包的所有内容:
from turtle import *


# 画个长方形
def draw_rectangle():
    # 设置笔刷宽度:
    width(4)

    # 前进:
    forward(200)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)

    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()


#
# if __name__ == '__main__':
#     draw_rectangle()


# 画星星
def draw_star_with_pos(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading:0
    seth(0)

    for i in range(5):
        fd(40)
        rt(144)


def draw_star():
    for x in range(0, 250, 50):
        draw_star_with_pos(x, 0)

    done()

# if __name__ == '__main__':
#     draw_star()
