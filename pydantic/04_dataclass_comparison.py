#!/usr/bin/python3
# This example shows how you can get dataclasses to smoothly serialize and
# deserialize. It uses the intution (prevalent in typescript) that the use of
# enum's is an antipattern since they do not "resolve" to a primitive type.
#
# Of additional note is that dataclasses **do not** do any sort of validation
# so you have to assume that the incoming data is "correct",
import json
import typing
from pydantic import BaseModel, PositiveInt
from dataclasses import dataclass, field, asdict


AthleticProwess = typing.Literal["ELITE", "MIDDLING", "POOR"]


@dataclass
class User:
    name: str = field(compare=True)
    age: int = field(compare=True)
    athletic_prowess: AthleticProwess = field(compare=False)


class UserValidated(BaseModel):
    name: str
    age: PositiveInt
    athletic_prowess: AthleticProwess


if __name__ == "__main__":
    u1 = User("Eric", 31, "ELITE")
    out_dict = json.dumps(asdict(u1))
    print(out_dict)

    in_dict = json.loads(out_dict)
    in_dict["athletic_prowess"] = "ELIT"  # data error
    u2 = User(**in_dict)
    print(u2)

    u3 = UserValidated(**in_dict)
    print(u3)
