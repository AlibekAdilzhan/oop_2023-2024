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

    def convert_gpa(self) -> float:
        gpa_2: float = self.__gpa / 4.0 * 5.0
        return gpa_2
    
    def __str__(self):
        return f"{self.surname} {self.course} {self.spec}"


st1 = Student("Aaa", "Bbb", 21, 4, "IT", 3.5)
print(st1)

# gpa_1 = 3.5
# gpa_2 = gpa_1 / 4 * 5