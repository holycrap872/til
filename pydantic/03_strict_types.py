# This example is different from `01_...` because it uses "strict" validation.
# This means that pydantic does not try to interpret strings as numbers (e.g.,
# "31" would through an error when passed to a `StrictInt`.
#!/usr/bin/python3
# This example shows the use of `Strict...` types that determines how pydantic
# parses (or refuses to parse) incoming values. In this case, we use the
# `StringInt` type to prevent pydantic from trying to interpret strings as
# integers.
#
# One thing to note is the difference between the usual `__init__()` function
# that ALWAYS does dynamic validation and the `construct()` which does not.
import enum
from pydantic import BaseModel
from pydantic.types import StrictStr, StrictInt


class AthleticProwess(enum.Enum):
    ELITE = "ELITE"
    MIDDLING = "MIDDLING"
    POOR = "POOR"


class User(BaseModel):
    name: str
    age: StrictInt
    athletic_prowess: AthleticProwess


if __name__ == "__main__":
    # vvvv Doesn't do dynamic validation vvvv
    u1 = User.construct(name="Eric", age="31", athletic_prowess=AthleticProwess.POOR)
    print(u1)

    # vvv Improper age type is both a static error and a dynamic error vvv
    u2 = User(name="Eric", age="31", athletic_prowess=AthleticProwess.ELITE)
    print(u2)
