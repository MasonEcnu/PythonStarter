#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hmac
# Keyed-Hashing for Message Authentication
import hmac

# key和message都是bytes类型
import random

msg = b"Hello World!"
key = b"secret"
h = hmac.new(key, msg, digestmod="MD5")
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())


def hmac_md5(key, s):
    return hmac.new(key.encode("utf-8"), s.encode("utf-8"), "MD5").hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = "".join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


user_db = {
    "michael": User("michael", "123456"),
    "bob": User("bob", "abc999"),
    "alice": User("alice", "alice2008")
}


def login(username, password):
    if username not in user_db:
        return False

    user = user_db[username]
    return user.password == hmac_md5(user.key, password)


assert login("michael", "123456")
assert login("bob", "abc999")
assert login("alice", "alice2008")
assert not login("michael", "1234567")
assert not login("bob", "123456")
assert not login("alice", "Alice2008")
print("ok")
