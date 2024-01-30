class Student:
    def __init__(self, name: str, surname: str, course: int, spec: str, age: int):
        self.name: str = name
        self.surname: str = surname
        self.course: int = course
        self.spec: str = spec
        self.age: int = age

    def __str__(self):
        return f"{self.name} {self.surname} {self.age}"
    
    def __add__(self, other_st: "Student"):
        new_name = self.name + other_st.name
        new_surname = self.surname + other_st.surname
        new_age = int(str(self.age) + str(other_st.age))
        new_course = self.course + other_st.course
        new_spec = self.spec + other_st.spec
        res_st = Student(new_name, new_surname, new_course, new_spec, new_age)
        return res_st
    


if __name__ == "__main__":
    a = 2
    b = 5
    print(a + b)
    st1 = Student("John", "Johnson", 3, "it", 26)
    st2 = Student("James", "Jameson", 2, "media", 23)
    st3 = st2 + st1
    print(st3)