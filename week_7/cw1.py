from dataclasses import dataclass

@dataclass
class Student:
    name: str
    surname: str
    age: int
    course: int
    spec: str
    __gpa: float

    def get_gpa(self) -> float:
        return self.__gpa 


st1 = Student("Aaa", "Bbb", 21, 4, "IT", 3.34)
print(st1.get_gpa())



