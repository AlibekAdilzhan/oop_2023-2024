class Rectangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.color = "red"

    def get_perimeter(self):
        p = (self.__a + self.__b) * 2
        return p
    
    def get_a(self):
        return self.__a

    def set_a(self, new_a):
        self.__a = new_a


# if __name__ == "__main__":
#     rect1 = Rectangle(3, 5)
#     print(rect1.a)
#     print(rect1.get_perimeter())

