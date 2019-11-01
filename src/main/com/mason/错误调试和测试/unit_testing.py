#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 单元测试
# “测试驱动开发”（TDD：Test-Driven Development）
import unittest


# 一个文件，只能有一个单元测试类
# 执行的是最后两行，按照定义顺序，取最新的


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):
    def test_init(self):
        print("TestDict......")
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self) -> None:
        print("SetUp......")

    def tearDown(self) -> None:
        print("TearDown......")


if __name__ == "__main__":
    unittest.main()


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError("成绩不能小于0或大于100: %d" % self.score)
        elif self.score >= 80:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student("Bart", 80)
        s2 = Student("Lisa", 100)
        self.assertEqual(s1.get_grade(), "A")
        self.assertEqual(s2.get_grade(), "A")

    def test_60_to_80(self):
        s1 = Student("Bart", 60)
        s2 = Student("Lisa", 79)
        self.assertEqual(s1.get_grade(), "B")
        self.assertEqual(s2.get_grade(), "B")

    def test_0_to_60(self):
        s1 = Student("Bart", 0)
        s2 = Student("Lisa", 59)
        self.assertEqual(s1.get_grade(), "C")
        self.assertEqual(s2.get_grade(), "C")

    def test_invalid(self):
        s1 = Student("Bart", -1)
        s2 = Student("Lisa", 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == "__main__":
    unittest.main()
