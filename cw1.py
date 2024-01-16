class Car:
    def __init__(self, name, eng_v, color, is_electro):
        self.car_name = name
        self.eng_v = eng_v
        self.car_color = color
        self.is_electro = is_electro
        self.x = 0

    def move_forward(self, dx):
        self.x = self.x + dx


if __name__ == "__main__":
    audi = Car("audi", 2.8, "black", False)
    print(audi.x)
    audi.move_forward(3)
    print(audi.x)
