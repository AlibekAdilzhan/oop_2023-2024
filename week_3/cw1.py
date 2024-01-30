class Employee:
    def __init__(self, name, surname, age, exp, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.experience = exp
        self.salary = salary

    def show_info(self):
        print(self.name, self.surname, self.age)

    def get_salary(self):
        return self.salary
    
    def set_salary(self, new_salary):
        self.salary = new_salary


class Teacher(Employee):
    def __init__(self, name, surname, age, exp, salary, subject):
        super().__init__(name, surname, age, exp, salary)
        self.teacher_sub = subject

    def show_info(self):
        print(self.name, self.surname, self.age, self.teacher_sub)


tea1 = Teacher("John", "Johnson", 29, 9, 890, "math")
tea1.show_info()