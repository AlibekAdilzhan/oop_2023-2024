from typing import List

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def get_info(self) -> str:
        s = f"{self.name} --- {self.age}"
        return s


class Faculty:
    def __init__(self, room_numb: int):
        self.students: List[Student] = []
        self.room_numb: int = room_numb


st1 = Student("Andrew", 21)
print(st1.get_info())