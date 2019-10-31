#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# asyncio
import asyncio
import threading


def test_hello():
    @asyncio.coroutine
    def hello():
        print("Hello world! (%s)" % threading.currentThread())
        yield from asyncio.sleep(1)
        print("Hello again! (%s)" % threading.currentThread())

    # 获取eventloop
    loop = asyncio.get_event_loop()
    # 执行coroutine
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


@asyncio.coroutine
def wget(host):
    print("wget %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
    writer.write(header.encode("utf-8"))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
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


if __name__ == "__main__":
    test_wget()
