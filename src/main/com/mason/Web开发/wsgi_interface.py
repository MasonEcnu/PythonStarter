#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# WSGI：Web Server Gateway Interface。
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    print(environ["PATH_INFO"])
    body = "<h1>Hello, %s!</h1>" % (environ["PATH_INFO"][1:] or "web")
    return [body.encode("utf-8")]


# 创建一个服务器，IP地址为空，端口为10101，处理函数为application
httpd = make_server("", 10101, application)
print("Serving HTTP on port 10101...")
httpd.serve_forever()
