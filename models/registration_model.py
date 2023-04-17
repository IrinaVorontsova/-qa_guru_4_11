from dataclasses import dataclass
from enum import Enum


class Hobbies(Enum):
    maths = "Maths"
    chemistry = "Chemistry"
    english = "English"
    biology = "Biology"
    science = "Computer Science"

@dataclass
class FormRegistration:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    birth_month: str
    birth_year: str
    birth_day: str
    interests: Hobbies
    hobby: str
    photo_path: str
    address: str
    state: str
    city: str

