#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# requests
import requests

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit"}
req = requests.get("https://www.baidu.com", params={"q": "python"}, headers=headers)
print(req.status_code)
print(req.content.decode("utf-8"))
print(req.url)
# print(req.json())

# post：data参数
url = "https://accounts.douban.com/login"
req = requests.post(url, data={"form_email": "abc@example.com", "form_password": "123456"})

params = {"key": "value"}
req = requests.post(url, json=params)  # 内部自动序列化为JSON

# 上传文件
upload_files = {"file": open(r"D:\PyCode\PythonStarter\src\main\resources\io_test.txt", "rb")}
req = requests.post(url, files=upload_files)

# 传cookies
cs = {'token': '12345', 'status': 'working'}
req = requests.get(url, cookies=cs, timeout=2.5)
