class Rectangle:
    def __init__(self, a: float, b: float):
        self.__a: float = a
        self.__b: float = b

    def area(self) -> float:
        return float(self.__a * self.__b)
    
    def get_a(self) -> float:
        return self.__a
    
    def get_b(self) -> float:
        return self.__b
    

class Circle:
    def __init__(self, r: float):
        self.__r = r

    def area(self):
        return self.__r**2 * 3.1415
    
    def get_r(self):
        return self.__r
    

