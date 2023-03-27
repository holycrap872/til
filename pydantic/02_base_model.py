#!/usr/bin/python3
# The "BaseModel" is the main class that usual users of Pydantic will interact
# with. It gives you the ability to easily define and validate certain data
# sets.
#
# This example shows how Pydantic can be used to serialize and deserialize
# enumerated types. Of further interest is the fact that it can take in a
# string age, and then it automatically parses it to an integer for us.
# (How to disable this behavior/catch it via typing is in later files)
import enum
from pydantic import BaseModel


class AthleticProwess(enum.Enum):
    ELITE = "ELITE"
    MIDDLING = "MIDDLING"
    POOR = "POOR"


class User(BaseModel):
    name: str
    age: int
    athletic_prowess: AthleticProwess


if __name__ == "__main__":
    # Note: the `"31"` is a 
    u = User(name="Eric", age="31", athletic_prowess=AthleticProwess.ELITE)
    json_dict = u.json()
    print(json_dict)
    u2 = User.parse_raw(json_dict)
    if u2.age > 21:
        print("hi")
    print(u2)
