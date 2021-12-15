# https://stackoverflow.com/questions/72263682/checking-input-data-types-in-pydantic
import enum
from pydantic import BaseModel
from pydantic.types import StrictStr, StrictInt


# Therefore, use custom __init__ to enforce input types at compile time


class Gender(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"



class User(BaseModel):
    name: StrictStr
    age: StrictInt
    gender: Gender

    def __init__(self, name: str, age: int, gender: Gender):
        super().__init__(name=name, age=age, gender=gender)


u = User(name="Eric", age="31", gender="31")
print(u)
