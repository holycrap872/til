#!/usr/bin/python3

import argparse
import typing
import random

def generator(file_path : str) -> None:
    with open(file_path, "w") as out_fd:
        for i in range(0, 1000):
            out_fd.write("{}, {}\n".format(i, random.randint(0, 300)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="path to file",
                        type=str, required=True)
    args = parser.parse_args()

    generator(args.file)
