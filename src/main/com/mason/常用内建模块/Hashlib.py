#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hashlib
# 摘要算法
import hashlib

# 128位
import random

md5 = hashlib.md5()
md5.update("how to use md5 in python hashlib?".encode("utf-8"))
print(md5.hexdigest())

# 160位
sha1 = hashlib.sha1()
sha1.update("how to use sha1 in ".encode("utf-8"))
sha1.update("python hashlib?".encode("utf-8"))
print(sha1.hexdigest())


# 摘要算法应用
# 以md5方式保存密码
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update((password + "the salt").encode("utf-8"))
    return md5.hexdigest()


db = {
    "michael": calc_md5("michael123"),
    "bob": calc_md5("bob456"),
    "alice": calc_md5("alice789")
}


def login(user, password):
    if user not in db:
        raise ValueError("not find user:%s in db" % user)
    p_md5 = calc_md5(password)
    if p_md5 != db[user]:
        raise ValueError("password is wrong for user:%s, password:%s" % (user, password))
    print("login successful.")


login("michael", "michael123")


# 练习2
def get_md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = "".join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


user_db = {
    "michael": User("michael", "123456"),
    "bob": User("bob", "abc999"),
    "alice": User("alice", "alice2008")
}


def register(username, password):
    db[username] = User(username, password)


def login(username, password):
    if username not in user_db:
        return False

    user = user_db[username]
    return user.password == get_md5(password + user.salt)


assert login("michael", "123456")
assert login("bob", "abc999")
assert login("alice", "alice2008")
assert not login("michael", "1234567")
assert not login("bob", "123456")
assert not login("alice", "Alice2008")
print("ok")
