#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# urllib
import json
from urllib import request

req = request.Request("http://www.douban.com/")
req.add_header("User-Agent",
               "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) "
               "AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
with request.urlopen(req) as page:
    data = page.read()
    print("Status:", page.status, page.reason)
    for k, v in page.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", data.decode("utf-8"))


# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入


# 练习
def fetch_data(url):
    req = request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) "
                   "AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")

    with request.urlopen(req) as page:
        return json.loads(page.read().decode("utf-8"))


URL = "https://www.liaoxuefeng.com/wiki/1016959663602400/1019223241745024"
data = fetch_data(URL)
print(data)
assert data["query"]["results"]["channel"]["location"]["city"] == "Beijing"
print("ok")
