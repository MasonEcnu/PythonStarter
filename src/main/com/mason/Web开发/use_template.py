#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用模板
# MVC：Model-View-Controller，中文名“模型-视图-控制器”
from flask import render_template, Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/signin", methods=["GET"])
def signin_form():
    return render_template("form.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "password":
        return render_template("signin-ok.html", username=username)
    return render_template("form.html", message="Bad username or password", username=username)


if __name__ == "__main__":
    app.run()
