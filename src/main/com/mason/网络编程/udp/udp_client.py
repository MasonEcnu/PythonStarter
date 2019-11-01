#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# UDP客户端
import socket


def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b"Michael", b"Tracy", b"Sarah"]:
        # 发送数据:
        client_socket.sendto(data, (host, port))
        # 接收数据:
        print(client_socket.recv(1024).decode("utf-8"))
    client_socket.close()


if __name__ == "__main__":
    start_client(host="127.0.0.1", port=10101)
