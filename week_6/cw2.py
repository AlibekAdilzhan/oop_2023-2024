class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        return f"{self.name} {self.age} {self.gender}"
    

class Doctor(Human):
    def __init__(self, name, age, gender, speciality):
        super().__init__(name, age, gender)
        self.spec = speciality

    def info(self):
        return f"{self.name} {self.age} {self.gender} {self.spec}"


d = Doctor("docok", 33, "m", "Surgery")

print(d.info())