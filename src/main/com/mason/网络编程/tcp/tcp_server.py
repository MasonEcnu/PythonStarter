#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tcp服务器
import socket
import threading


def tcp_link(sock, addr):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b"Welcome!")
    while True:
        data = sock.recv(1024)
        # time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(("Hello, %s!" % data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print("Connection from %s:%s closed." % addr)


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定监听地址和端口
    server_socket.bind((host, port))

    # 等待连接的最大数量
    server_socket.listen(5)
    print("Waiting for connection...")

    # 启动服务器
    while True:
        # 接受一个新连接
        sock, addr = server_socket.accept()
        # 创建新的线程来处理客户端连接
        th = threading.Thread(target=tcp_link, args=(sock, addr))
        th.start()


if __name__ == "__main__":
    start_server(host="127.0.0.1", port=10101)
