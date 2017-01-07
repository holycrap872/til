#!/usr/bin/python3

import argparse
import typing
import random
import sys

def reducer() -> None:
    running_sum = 0
    running_total = 0

    for line in sys.stdin:
        pieces = line.split(",")
        piece_sum = int(pieces[0])
        piece_num = int(pieces[1])

        running_sum += piece_sum
        running_total += piece_num

    print("{}".format(running_sum / running_total))

if __name__ == "__main__":
    reducer()
