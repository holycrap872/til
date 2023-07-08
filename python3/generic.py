#!/usr/bin/python3
import argparse

def function(a, b, c, this, that):
    print(a, b, c, this, that)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="option a",
                        type=str, required=True, nargs='*')
    parser.add_argument("-b", "--bee", help="option bee",
                        default= None, type=str, required=False)
    parser.add_argument("-c", "--sea", help="option sea",
                        default=False, required=False, action='store_true')
    this_or_that = parser.add_mutually_exclusive_group(required=True)
    this_or_that.add_argument("--this", help="What dis", type=str)
    this_or_that.add_argument("--that", help="What dat", type=str)
    args = parser.parse_args()

    function(args.a, args.bee, args.sea, args.this, args.that)
