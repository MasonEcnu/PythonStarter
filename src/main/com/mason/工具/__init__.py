# 写一些实用工具
import random


def random_list(n, start=0, end=10):
    ll = []
    randint = random.randint
    for i in range(n):
        ll.append(randint(start, end))
    return ll


if __name__ == '__main__':
    print(random_list(0))
