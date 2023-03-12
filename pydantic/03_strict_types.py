# This example is different from `01_...` because it uses "strict" validation.
# This means that pydantic does not try to interpret strings as numbers (e.g.,
# "31" would through an error when passed to a `StrictInt`.
import enum
from pydantic import BaseModel
from pydantic.types import StrictStr, StrictInt


class AthleticProwess(enum.Enum):
    ELITE = "ELITE"
    MIDDLING = "MIDDLING"
    POOR = "POOR"


class User(BaseModel):
    name: StrictStr
    age: StrictInt
    athletic_prowess: AthleticProwess


# vvvv Doesn't do dynamic validation vvvv
u1 = User.construct(name="Eric", age="31", athletic_prowess=AthleticProwess.POOR)
print(u1)

# vvv Improper age type is both a static error and a dynamic error vvv
u2 = User(name="Eric", age="31", athletic_prowess=AthleticProwess.ELITE)
print(u2)
