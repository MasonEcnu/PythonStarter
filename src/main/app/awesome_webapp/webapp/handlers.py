#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# url逻辑处理
import hashlib
import json
import logging
import re
import time

from aiohttp import web

from src.main.app.awesome_webapp.webapp.apis import APIValueError, APIError
from src.main.app.awesome_webapp.webapp.config import configs
from src.main.app.awesome_webapp.webapp.core_web import get, post
from src.main.app.awesome_webapp.webapp.models import Blog, User, next_id

"""
以下为测试代码
"""


@get("/")
def index(request):
    summary = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, " \
              "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    blogs = [
        Blog(id="1", name="Test Blog", summary=summary, created_at=time.time() - 120),
        Blog(id="2", name="Something New", summary=summary, created_at=time.time() - 3600),
        Blog(id="3", name="Learn Swift", summary=summary, created_at=time.time() - 7200)
    ]
    return {
        "__template__": "blogs.html",
        "blogs": blogs
    }


@get("/api/users")
async def api_get_users():
    users = await User.find_all(order_by="create_time desc")
    for u in users:
        u.password = "******"
    return dict(users=users)


"""
以下为正式代码
"""

COOKIE_NAME = "mason-webapp"
_COOKIE_KEY = configs.session.secret
COOKIE_MAX_AGE = 86400


def user_to_cookie(user):
    """
    Generate cookie str by user
    :param user:
    :param max_age:
    :return:
    """
    # build cookie string by:id-expires-sha1
    expires = str(int(time.time() + COOKIE_MAX_AGE))
    s = "%s-%s-%s-%s" % (user.id, user.password, expires, _COOKIE_KEY)
    cookie_list = [user.id, expires, hashlib.sha1(s.encode("utf-8")).hexdigest()]
    return "-".join(cookie_list)


async def cookie_to_user(cookie_str):
    """
    Parse cookie and load user if cookie is valid
    :param cookie_str:
    :return:
    """
    if not cookie_str:
        return None

    try:
        cookie_list = cookie_str.split("-")
        if len(cookie_list) != 3:
            return None

        uid, expires, sha1 = cookie_list
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None

        s = "%s-%s-%s-%s" % (user.id, user.password, expires, _COOKIE_KEY)

        if sha1 != hashlib.sha1(s.encode("utf-8")).hexdigest():
            logging.info("invalid sha1 for user:%s" % user.name)
            return None

        user.password = "******"
        return user
    except Exception as e:
        logging.exception(e)
        return None


@get("/register")
def register():
    return {
        "__template__": "register.html"
    }


@get("/signin")
def signin():
    return {
        "__template__": "signin.html"
    }


@post("/api/authenticate")
async def authenticate(*, email, password):
    if not email:
        raise APIValueError("email", "Invalid email.")
    if not password:
        raise APIValueError("password", "Invalid password.")

    users = await User.find_all("email=?", [email])
    if len(users) == 0:
        raise APIValueError("email", "Email not exist.")

    user = users[0]
    # check password
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode("utf-8"))
    sha1.update(b":")
    sha1.update(password.encode("utf-8"))

    if user.password != sha1.hexdigest():
        raise APIValueError("password", "Invalid password")

    # authenticate ok, set cookie:
    resp = web.Response()
    resp.set_cookie(COOKIE_NAME, user_to_cookie(user), max_age=COOKIE_MAX_AGE, httponly=True)
    user.password = "******"
    resp.content_type = "application/json"
    resp.body = json.dumps(user, ensure_ascii=False).encode("utf-8")
    return resp


@get("/signout")
def signout(request):
    referer = request.headers.get("Referer")
    resp = web.HTTPFound(referer or "/")
    resp.set_cookie(COOKIE_NAME, "-deleted-", max_age=0, httponly=True)
    logging.info("user sign out.")
    return resp


_RE_EMAIL = re.compile(r"^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$")
_RE_SHA1 = re.compile(r"^[0-9a-f]{40}$")


@post("/api/users")
async def api_register_user(*, name, email, password):
    if not name or not name.strip():
        raise APIValueError("name")

    if not email or not _RE_EMAIL.match(email):
        raise APIValueError("email")

    if not password or not _RE_SHA1.match(password):
        raise APIValueError("password")

    user = await User.find_all("email=?", [email])
    if len(user) > 0:
        raise APIError("register:failed", "email", "Email is already in use.")

    uid = next_id()
    sha1_password = "%s:%s" % (uid, password)
    user = User(
        id=uid,
        name=name.strip(),
        admin=True if name.strip().lower() == "mason" else False,
        password=hashlib.sha1(sha1_password.encode('utf-8')).hexdigest(),
        email=email,
        image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest()
    )
    await user.save()
    # make session cookie
    resp = web.Response()
    resp.set_cookie(COOKIE_NAME, user_to_cookie(user), max_age=COOKIE_MAX_AGE, httponly=True)
    user.password = "******"
    resp.content_type = "application/json"
    resp.body = json.dumps(user, ensure_ascii=False).encode("utf-8")
    return resp
