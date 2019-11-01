#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 本地配置文件

'''
Default configurations.
'''

__author__ = "Mason.Wu"

configs = {
    "db": {
        "host": "127.0.0.0",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "awesome_app"
    },
    "session": {
        "secret": "Hello World!"
    }
}
