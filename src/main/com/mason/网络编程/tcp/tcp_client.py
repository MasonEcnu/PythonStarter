#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tcp客户端
import socket


def test_http_tcp():
    # SOCK_STREAM指定使用面向流的TCP协议
    # AF_INET:ipv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.sina.com.cn", 80))
    # 发送数据
    s.send(b"GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n")

    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b"".join(buffer)

    s.close()

    header, html = data.split(b"\r\n\r\n", 1)
    print(header.decode("utf-8"))
    # 把接收的数据写入文件:
    with open(r"D:\PyCode\PythonStarter\src\main\resources\sina.html", "wb") as f:
        f.write(html)


def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定监听地址和端口
    client_socket.connect((host, port))
    # 接收欢迎消息:
    print(client_socket.recv(1024).decode("utf-8"))
    for data in [b"Michael", b"Tracy", b"Sarah"]:
        # 发送数据:
        client_socket.send(data)
        print(client_socket.recv(1024).decode("utf-8"))
    client_socket.send(b"exit")
    client_socket.close()


if __name__ == "__main__":
    start_client(host="127.0.0.1", port=10101)
