#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pillow
# PIL：Python Imaging Library
import random

from PIL import Image, ImageFilter, ImageFont, ImageDraw

# 操作图像
base_url = r"D:\PyCode\PythonStarter\src\main\resources"
img = Image.open(base_url + r"\test_pillow.jpeg")
new_img = img.filter(ImageFilter.BLUR)
new_img.save(base_url + r"\filter_blue_test_pillow.jpg", "jpeg")


# # 缩放到50%:
# im.thumbnail((w//2, h//2))

# 图片验证码
# 随机字母
def random_char():
    return chr(random.randint(33, 126))


def random_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def random_second_color():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def gen_picture_verify_code(path):
    # 验证码大小
    width = 60 * 4
    height = 60

    image = Image.new("RGB", (width, height), (255, 255, 255))
    # 创建Font对象
    font = ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf", 36)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=random_color())
    for t in range(4):
        draw.text((60 * t + 10, 10), random_char(), font=font, fill=random_second_color())

    # 模糊
    image = image.filter(ImageFilter.BLUR)
    image.save(path + r"\picture_verify_code.jpg", "jpeg")


if __name__ == '__main__':
    gen_picture_verify_code(base_url)
