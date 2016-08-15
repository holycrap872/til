#!/usr/bin/python3
import argparse

def function(a, b, c):
    print(a, b, c)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="option a",
                        type=str, required=True, nargs='*')
    parser.add_argument("-b", "--bee", help="option bee",
                        default= None, type=str, required=False)
    parser.add_argument("-c", "--sea", help="option sea",
                        default=False, required=False, action='store_true')
    args = parser.parse_args()

    function(args.a, args.bee, args.sea)
