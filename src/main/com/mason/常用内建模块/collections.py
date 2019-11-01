#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# collections

# namedtuple
# tuple可以表示不变集合
import argparse
import os
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter

# 点坐标
point = (1, 2)

Point = namedtuple("Point", ["x", "y"])

point = Point(1, 2)
print(point.x)
print(point.y)

Circle = namedtuple("Circle", ["x", "y", "z"])

# deque--双端队列
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
dq = deque(["a", "b", "c"])
dq.append("d")
dq.appendleft("1")
print(dq)
dq.popleft()
print(dq)

# defaultdict
dd = defaultdict(lambda: "None")
dd["key1"] = "key1"
print(dd["key2"])

# OrderedDict
od = OrderedDict([("f", 1), ("a", 2), ("e", 3)])
print(od)


# FIFO的dict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self) - contains_key >= self._capacity:
            last = self.popitem(last=False)
            print("remove:", last)
        if contains_key:
            del self[key]
            print("set:", (key, value))
        else:
            print("add:", (key, value))
        OrderedDict.__setitem__(self, key, value)


# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict

# 构造缺省参数
defaults = {
    "color": "red",
    "user": "guest"
}

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user")
parser.add_argument("-c", "--color")
namespace = parser.parse_args()
command_line_args = {
    k: v for k, v in vars(namespace).items() if v
}

# 组合成ChainMap
# 优先级map
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数
print("color:", combined["color"])
print("user:", combined["user"])

# Counter
# Counter是一个简单的计数器

ct = Counter()
for ch in "programing":
    ct[ch] += 1

print(ct)
