#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用Mysql
import mysql.connector


# MySQL的SQL占位符是%s
def test_mysql():
    conn = mysql.connector.connect(user="root", password="123456", database="python_demo")
    cursor = conn.cursor()
    # 创建user表
    cursor.execute("create table if not exists user (id varchar(20) primary key, name varchar(20))")
    # 插入记录
    cursor.execute("insert into user (id, name) values (%s, %s)", ["1", "Mason"])
    print(cursor.rowcount)
    # 执行查询
    cursor.execute("select * from user")
    values = cursor.fetchall()
    print(values)
    # 提交事务
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    test_mysql()
