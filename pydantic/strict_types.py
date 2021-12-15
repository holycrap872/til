# https://stackoverflow.com/questions/72263682/checking-input-data-types-in-pydantic
import enum
from pydantic import BaseModel
from pydantic.types import StrictStr, StrictInt


# Data inputs to models at run-time but not at compile time


class Gender(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"



class User(BaseModel):
    name: StrictStr
    age: StrictInt
    gender: Gender


u = User(name="Eric", age="31", gender="31")
print(u)
