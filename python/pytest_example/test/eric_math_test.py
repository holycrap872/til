import pytest

from pytest_example.eric_math import *

def test_square_1():
    assert square(3) == 9
    assert square(0) == 0

def test_square_2():
    assert square(5) == square(4) + square(3)
