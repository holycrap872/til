# Iterators vs. Iterables
# IteraBLES are things that we can loop through
# IteraTORS are a particular run through an iterable
import typing


def print_iterable(items: typing.Iterable) -> None:
    """
    Iterables can be used to create _new_ iterators, basically meaning that
    they **can be** reset.
    """
    print("Printing iterABLE")
    for i in items:
        print(i)

    print("Printing iterABLE again")
    for i in items:
        print(i)

    print("Done printing iterABLE")


def print_iterator(items: typing.Iterable) -> None:
    """
    Iterators are a **particular** run through a bunch of iterms, meaning
    that they **cannot be** reset.
    """
    print("Printing iterATOR")
    for i in items:
        print(i)

    print("Printing iterATOR")
    for i in items:
        print(i)

    print("Done printing iterATOR")


if __name__ == "__main__":
    items = ("rope", "knife", "mask")
    print_iterable(items)
    print_iterable(iter(items))
