#!/usr/bin/python3.4
import typing

class Person():
    def __init__(self, name : str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    @staticmethod
    def factory(name: str) -> Person:
        return Person(name)

def add_int(x: int, y: int) -> int:
    return x + y

def greet_all(names: typing.Iterable[str]) -> None:
    for name in names:
        print("Hello {0}".format(name))

def main() -> None:
    add_int(5, 6)
    add_int('c', 'l')

    greet_all(["Eric", "John", "Bill"])
    greet_all(["Eric", "John", 0])

    person = Person.factory("Eric")
    print(person.get_name())

    person = Person.factory(0)
    print(person.get_name())


# ```
# sudo apt-get install python3 python3-pip
# sudo pip3 install mypy-lang
# mypy typing_example.py
# ```
if __name__ == "__main__":
    main()
