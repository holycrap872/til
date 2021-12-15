import enum
from pydantic import BaseModel


class Gender(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"



class User(BaseModel):
    name: str
    age: int
    gender: Gender = Gender.OTHER


u = User(name="Eric", age=31)
json_dict = u.json()
print(json_dict)
u2 = User.parse_raw(json_dict)
if u2.age > "21":
    print("hi")
print(u2)
