import pytest

from pytest_example.eric_strings import *

def test_stringify_array_1():
    assert stringify_array(['hi', 'eric']) == "hi eric"

def test_stringify_array_2():
    assert stringify_array(['hi']) == "hi"

def test_stringify_array_3():
    assert stringify_array(["yes ", "mam"]) == "yes  mam"

