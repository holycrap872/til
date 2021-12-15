import enum
import json
import typing


class Skater(str, enum.Enum):
    COOL = "COOL"
    JOSH = "JOSH"


class Person(typing.NamedTuple):
    name: str
    age: int
    skate: Skater


p1 = Person("Chad", "33", Skater.COOL)
print(p1)
json_str = json.dumps(p1)
print(json_str)

p2 = Person(*json.loads(json_str))
print(p2)

breakpoint()
assert p1 == p2
