#!/usr/bin/python3

import argparse
import typing
import random
import sys

def mapper() -> None:
    running_sum = 0
    running_total = 0
    for line in sys.stdin:
        pieces = line.split(",")
        identifer = int(pieces[0])
        amount = int(pieces[1])

        running_sum += amount
        running_total += 1

    print("{},{}".format(running_sum, running_total))

if __name__ == "__main__":
    mapper()

