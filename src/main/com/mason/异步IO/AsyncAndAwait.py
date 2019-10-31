#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# asyncio
import asyncio
import threading


# @asyncio.coroutine和yield from
# 等价于
# async和await
def test_hello():
    async def hello():
        print("Hello world! (%s)" % threading.currentThread())
        await asyncio.sleep(1)
        print("Hello again! (%s)" % threading.currentThread())

    # 获取eventloop
    loop = asyncio.get_event_loop()
    # 执行coroutine
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


# if __name__ == '__main__':
#     test_hello()


async def wget(host):
    print("wget %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
    writer.write(header.encode("utf-8"))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()


def test_wget():
    # 获取eventloop
    loop = asyncio.get_event_loop()
    # 执行coroutine
    tasks = [wget(host) for host in ["www.sina.com.cn", "www.sohu.com", "www.163.com"]]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    test_wget()
