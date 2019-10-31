#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用web框架
# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1>Welcome home!</h1>"


@app.route("/signin", methods=["GET"])
def signin_form():
    return """<form action="/signin" method="POST">
    <p><input name="username"/></p>
    <p><input name="password" type="password"/></p>
    <p><button type="submit">Sign In</button></p>
    </from>"""


@app.route("/signin", methods=["POST"])
def signin():
    # 需要从request对象中读取表单内容
    if request.form["username"] == "admin" and request.form["password"] == "password":
        return "<h1>Hello, admin!</h1>"
    return "<h1>Bad username or password.</h1>"


# flask默认端口为5000
if __name__ == '__main__':
    app.run()
