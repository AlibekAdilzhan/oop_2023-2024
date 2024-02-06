class Rectangle:
    def __init__(self, a: float, b: float):
        self.__a: float = a
        self.__b: float = b

    def get_perimeter(self) -> float:
        return (self.__a + self.__b) * 2
    
    def get_area(self) -> float:
        return self.__a * self.__b
         
    def get_a(self) -> float:
        return self.__a
    
    def get_b(self) -> float:
        return self.__b


# if __name__ == "__main__":
#     rect1 = Rectangle(3, 5)
#     assert rect1.get_area() == 15, "wrong area"
#     assert rect1.get_perimeter() == 16, "wrong perimeter"
