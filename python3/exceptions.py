#!/usr/bin/python3
import argparse
import typing
import traceback


class ExampleException(Exception):
    def __init__(self, *args, **kwargs) -> None:
        Exception.__init__(self, *args, **kwargs)


def raise_exception(num : int) -> None:
    for i in range(0, num):
        try:
            raise ExampleException("Exception number {}".format(num))

        except ExampleException as e:
            print(e)
#            traceback.print_stack(e)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", help="Number of exceptions to raise",
                        type=int, required=True)
    args = parser.parse_args()

    raise_exception(args.num)
