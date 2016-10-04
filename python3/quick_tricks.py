#!/usr/bin/python3

import binascii
import collections
import json

def formating():
    string = "Number 1: {0}, Number 2: {1:+012b}, Number 3: {2:010d}"
    string = string.format(4, 6, -9)

    assert string == "Number 1: 4, Number 2: +00000000110, Number 3: -000000009"

## The `str.encode()` method doesn't seem to have made it's way from 2.7 to 3.x
## This is how you create various "hexification" of strings
def encode_decode_hex():
    string_binary = b"this is a test"
    hex_string_binary = binascii.hexlify(string_binary)
    assert str(hex_string_binary) == "b'7468697320697320612074657374'"
    assert str(hex_string_binary, "ascii") == "7468697320697320612074657374"

    string_binary = binascii.unhexlify(hex_string_binary)
    assert str(string_binary) == "b'this is a test'"
    assert str(string_binary, "ascii") == "this is a test"


Person = collections.namedtuple("Person", "name age")
def named_tuples():
    person = Person("eric", 56)
    print("Name: {0} Age: {1}".format(person.name, person.age))


def enum(file_path):
    with open(file_path, "r") as f:
        for lineno, line in enumerate(f, start=1):
            print("Line {0}, Line Number: {1}".format(line, lineno))


def default_dictionary(word_list):
    counter = collections.defaultdict(int) # By default, `int` returns 0
    for word in word_list:
        counter[word] += 1


def set():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1 |= set2  # union


def set_comp(max_int):
    return {num for num in range(0, max_int)}


## Lambda's work as unnamed functions on elements of a list.  In this case,
## each elem (``e`) is treated as a tuple and reveresed.  The normal recursive
## sort occurs, at which point the values are returned to their original value
def lambda():
    x = [(1, 10), (2, 9), (3, 8)]
    x.sort(key=lambda e: (e[1], e[0]))
    assert x == [(3, 8), (2, 9), (1, 10)]


def lambda2():
    x = [1,2,3,4,5]
    x.sort(key=lambda e: 1 if x < 3 else 0)

    assert x == [4, 5 , 1, 2 , 3]


def json_eval():
    x = json.loads('{"1":"a","2":"b"}')
    assert x['1'] == 'a'


def enumerate_dictioary():
    x = {1:'a', 2, 'z'}
    for count, key in enumerate(x):
        # count starts at 0
        print("{}: {} -> {}".format(count, key, x[key])
