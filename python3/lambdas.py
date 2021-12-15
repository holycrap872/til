#!/usr/bin/env python3
from operator import mul
from functools import reduce


def map_1() -> None:
    arr = [1, 2, 3, 4]
    print(list(map(lambda x: x + 1, arr)))


def map_2() -> None:
    arr_1 = [1, 2, 3, 4]
    arr_2 = [10, 20, 30, 40]
    print(list(map(lambda x, y: x + y, arr_1, arr_2)))


# The What’s New In Python 3.0 guide reinforces this idea when it says the
# following: Use functools.reduce() if you really need it; however, 99 percent
# of the time an explicit for loop is more readable. (Source)

def reduce_1() -> None:
    arr = [1, 2, 3, 4]
    print(reduce(lambda acc, y: acc + y, arr))


def reduce_as_len() -> None:
    arr = [18, 4, -10, 99, 100]
    print(reduce(lambda acc, y: acc + 1, arr, 0))


def reduce_mul() -> None:
    arr = [10, 10, 10]
    print(reduce(mul, arr))


def reduce_min() -> None:
    arr = [18, 4, -10, 99, 100]
    print(reduce(lambda acc, y: acc if acc < y else y, arr))


map_1()
map_2()
reduce_1()
reduce_as_len()
reduce_mul()
reduce_min()
