#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# UDP服务器
import socket


def start_server(host, port):
    # SOCK_DGRAM:使用UDP协议建立socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    server_socket.bind((host, port))

    print("Bind UDP port on:", port)
    while True:
        # 接收数据
        data, addr = server_socket.recvfrom(1024)
        print("Received data from %s:%s." % addr)
        server_socket.sendto(b"Hello %s!" % data, addr)


if __name__ == "__main__":
    start_server(host="127.0.0.1", port=10101)
