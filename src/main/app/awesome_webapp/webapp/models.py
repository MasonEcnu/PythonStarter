#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
import asyncio
import time
import uuid

from src.main.app.awesome_webapp.webapp import orm
from src.main.app.awesome_webapp.webapp.orm import Model, StringField, BooleanField, FloatField, TextField


def next_id():
    return "%015d%s000" % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = "users"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    name = StringField(ddl="varchar(50)")
    admin = BooleanField()
    password = StringField(ddl="varchar(50)")
    email = StringField(ddl="varchar(50)")
    image = StringField(ddl="varchar(500)")
    create_time = FloatField(default=time.time)


class Blog(Model):
    __table__ = "blogs"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    name = StringField(ddl="varchar(50)")
    summary = StringField(ddl="varchar(200)")
    content = TextField()
    create_time = FloatField(default=time.time)


class Comment(Model):
    __table__ = "comments"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    blog_id = StringField(ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    content = TextField()
    create_time = FloatField(default=time.time)


async def test_save_user(loop):
    kw = {
        "user": "root",
        "password": "123456",
        "db": "awesome_app"
    }
    await orm.create_pool(loop, **kw)
    u = User(name="Mason", admin=True, password="admin", email="364206176@qq.com", image="about:blank")
    await u.save()


async def test_other_method(loop):
    kw = {
        "user": "root",
        "password": "123456",
        "db": "awesome_app"
    }
    await orm.create_pool(loop, **kw)
    # 1. 测试测试插入
    u = User(name="Mason", admin=True, password="admin", email="364206176@qq.com", image="about:blank")
    await u.save()

    uid = "0015725820548948396299028024fe0bd847cbc5b847330000"
    # 2. 测试根据主键查询方法
    # u = await User.find(uid)
    # print(u)

    # 3. 测试根据参数查询方法
    # u = await User.find_all(where="name like ?", args=["%m%"], orderBy="name asc", limit=(0, 10))
    # print(u)

    # 4. 测试findNumber方法，不知道这个方法有什么用
    # u_count = await User.find_count("name")
    # print(u_count)

    # 5. 测试更新方法
    # u = await User.find(uid)
    # u["password"] = "hello world"
    # await u.renewal()

    # 6. 测试删除方法
    # u = await User.find(uid)
    # await u.remove()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_other_method(loop))
    print("execute finished.")
