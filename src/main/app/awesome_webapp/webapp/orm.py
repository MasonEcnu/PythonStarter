#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对象关系映射文件
# 数据库处理
import asyncio
import logging

import aiomysql


def log(sql, args=()):
    logging.info("SQL: %s, args:%s" % (sql, args))


async def create_pool(loop, **kw):
    logging.info("create database connection pool...")
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get("host", "127.0.0.1"),
        port=kw.get("port", 3306),
        user=kw["user"],
        password=kw["password"],
        db=kw["db"],
        charset=kw.get("charset", "utf8"),
        autocommit=kw.get("autocommit", True),
        maxsize=kw.get("maxsize", 10),
        minsize=kw.get("minsize", 1),
        loop=loop
    )


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace("?", "%s"), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info("rows returned:%s" % len(rs))
        return rs


# insert, update, delete
async def execute(sql, args):
    log(sql, args)
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace("?", "%s"), args)
            affected = cur.rowcount
            await cur.close()
        except BaseException:
            raise
        return affected


# ORM
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return "<%s, %s:%s>" % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl="varchar(100)"):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, "boolean", False, default)


class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, "bigint", primary_key, default)


class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, "real", primary_key, default)


class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, "text", False, default)


def create_args_string(num):
    L = []
    for n in range(num):
        L.append("?")
    return ", ".join(L)


class ModelMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        # 排除Model类本身
        if name == "Model":
            return type.__new__(mcs, name, bases, attrs)
        # 获取table名称
        table_name = attrs.get("__table__", None) or name
        logging.info("found model:%s (table:%s)" % (name, table_name))
        # 获取所有的Field和主键名
        mappings = dict()
        fields = []
        primary_key = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info("  found mapping:%s ==> %s" % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键
                    if primary_key:
                        raise RuntimeError("Duplicate primary key for field:%s" % k)
                    primary_key = k
                else:
                    fields.append(k)
        if not primary_key:
            raise RuntimeError("Primary key not found in table:%s" % table_name)
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))

        attrs["__mappings__"] = mappings  # 保存属性和列的映射关系
        attrs["__table__"] = table_name
        attrs["__primary_key__"] = primary_key  # 主键属性名
        attrs["__fields__"] = fields  # 除主键外的属性名
        # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
        attrs["__select__"] = "select `%s`, %s from `%s`" % (primary_key, ", ".join(escaped_fields), table_name)
        attrs["__insert__"] = "insert into `%s` (%s, `%s`) values (%s)" % (
            table_name, ", ".join(escaped_fields), primary_key, create_args_string(len(escaped_fields) + 1))
        attrs["__update__"] = "update `%s` set %s where `%s`=?" % (
            table_name, ", ".join(map(lambda f: "`%s`=?" % (mappings.get(f).name or f), fields)), primary_key)
        attrs["__delete__"] = "delete from `%s` where `%s`=?" % (table_name, primary_key)
        return type.__new__(mcs, name, bases, attrs)


# Model
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def get_value(self, key):
        return getattr(self, key, None)

    def get_value_or_default(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug("using default value for %%:%s" % key, str(value))
                setattr(self, key, value)
        return value

    @classmethod
    async def find(cls, pk):
        "find object by primary key."
        rs = await select("%s where `%s`=?" % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    @classmethod
    async def find_all(cls, where=None, args=None, **kw):
        "find all objects by where clause."
        sql = [cls.__select__]
        if where:
            sql.append("where")
            sql.append(where)

        if args is None:
            args = []

        order_by = kw.get("order_by", None)
        if order_by:
            sql.append("order by")
            sql.append(order_by)

        limit = kw.get("limit", None)
        if limit is not None:
            sql.append("limit")
            if isinstance(limit, int):
                sql.append("?")
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append("?,?")
                args.extend(limit)
            else:
                raise ValueError("Invalid limit value:%s" % str(limit))

        rs = await select(" ".join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def find_count(cls, select_field, where=None, args=None):
        "find count by select and where"
        sql = ["select count(%s) as num from `%s`" % (select_field, cls.__table__)]
        if where:
            sql.append("where")
            sql.append(where)

        rs = await select(" ".join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]["num"]

    async def save(self):
        args = list(map(self.get_value_or_default, self.__fields__))
        args.append(self.get_value_or_default(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warning("failed to insert record: affected rows:%s" % rows)
        return rows

    async def renewal(self):
        "equal to update"
        args = list(map(self.get_value_or_default, self.__fields__))
        args.append(self.get_value_or_default(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warning("failed to update record by primary key: affected rows:%s" % rows)
        return rows

    async def remove(self):
        args = [self.get_value(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warning("failed to delete record by primary key: affected rows:%s" % rows)
        return rows


if __name__ == "__main__":
    kw = {
        "user": "root",
        "password": "123456",
        "db": "python_demo"
    }
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_pool(loop, **kw))
