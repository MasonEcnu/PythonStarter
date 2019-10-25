#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列化
# 把变量从内存中变成可存储或传输的过程称之为序列化
# pickling--unpickling
# pickle.dump()直接把对象序列化后写入一个file-like Object
# pickle--python专享的序列化包
import json
import pickle

d = dict(name="Mason", age=22, gender="Male")
pickled_d = pickle.dumps(d)
print(pickled_d)
unpickled_d = pickle.loads(pickled_d)
print(unpickled_d)

# load():从文件中导入bytes
# load():直接将bytes转为object


# json
# JSON类型	Python类型
# {}	dict
# []	list
# "string"	str
# 1234.56	int或float
# true/false	True/False
# null	None

json_d = json.dumps(d)
print(json_d)
unjson_d = json.loads(json_d)
print(unjson_d)


# python进阶
class Student(object):
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return "name:%s, age:%d, gender:%s, score:%.2f" % (self.name, self.age, self.gender, self.score)


def dict_to_student(d):
    return Student(d["name"], d["age"], d["gender"], d["score"])


def student_to_dict(stu):
    return {
        "name": stu.name,
        "age": stu.age,
        "gender": stu.gender,
        "score": stu.score
    }


stu = Student("Mason", 22, "Male", 80)
# default=student_to_dict
# default=lambda obj: obj.__dict__
# ensure_ascii=转码
json_stu = json.dumps(stu, default=student_to_dict, ensure_ascii=True)
print(json_stu)
unjson_stu = json.loads(json_stu, object_hook=dict_to_student)
print(unjson_stu)

obj = dict(name="小明", age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
