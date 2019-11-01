#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用SQLite
import os
import sqlite3

db_file_path = r"D:\PyCode\PythonStarter\src\main\resources\test.db"


# # sqllite的占位符是?
# 打开后一定记得关闭
def test_sqllite3():
    # 连接到SQLLite数据库
    # 数据库文件名问test.db
    # 如果文件不存在，则创建
    conn = sqlite3.connect(db_file_path)
    # 创建一个游标
    cursor = conn.cursor()
    print(type(cursor))
    # 执行建表语句
    cursor.execute("create table if not exists user (id varchar(20) primary key, name varchar(10))")
    # 继续执行插入语句
    cursor.execute("insert into user (id, name) values ('2','Mason')")
    # 获取插入的行数
    print(cursor.rowcount)
    # 获取插入的结果
    cursor.execute("select * from user where id=?", ("1",))
    values = cursor.fetchall()
    print(values)
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()


#
# if __name__ == '__main__':
#     test_sqllite3()


# 练习
db_file = os.path.join(os.path.dirname(__file__), db_file_path)
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def second(elem):
    return elem[2]


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    result = []
    try:
        cursor.execute("select id, name, score from user")
        values = cursor.fetchall()
        values.sort(key=second)
        for user in values:
            score = int(user[2])
            if low <= score <= high:
                result.append(user[1])
    finally:
        cursor.close()
        conn.close()
    return result


if __name__ == '__main__':
    assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
    assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
    print("Ok")
