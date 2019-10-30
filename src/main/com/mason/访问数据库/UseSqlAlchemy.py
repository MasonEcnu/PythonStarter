#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用SqlAlchemy
# ORM技术：Object-Relational Mapping

# 第一步，导入SQLAlchemy，并初始化DBSession：

# 创建对象的基类
from sqlalchemy import Column, String, create_engine, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# 定义user类
class User(Base):
    # 表名
    __tablename__ = "user"

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# "数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名"
# 初始化数据库连接
engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/python_demo")
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)


def insert_user(user):
    ids = query_user_ids()
    if isinstance(user, User):
        if user.id in ids:
            raise TypeError("Repeated injection is forbidden:%s" % user.id)
        # 创建DBSession对象
        session = DBSession()
        # 将user添加到session
        session.add(user)
        # 提交
        session.commit()
        # 关闭
        session.close()
    else:
        raise TypeError("Insert type error:%s, type:%s" % (user, type(user)))


def query_user():
    # 创建DBSession对象
    session = DBSession()
    # 将user添加到session
    result = list(session.query(User).all())
    # 关闭
    session.close()
    return result


def query_user_ids():
    # 创建DBSession对象
    session = DBSession()
    # 将user添加到session
    # filter是where条件
    result = []
    for u in session.query(User).all():
        result.append(u.id)
    # 关闭
    session.close()
    return result


if __name__ == '__main__':
    insert_user(User(id="2", name="Hello"))


# 一对多关系
class School(Base):
    __tablename = "school"

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多
    clazz = relationship("Clazz")


class Clazz(Base):
    __tablename = "clazz"

    # 表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    # 一对多
    school_id = Column(String(20), ForeignKey("school.id"))
