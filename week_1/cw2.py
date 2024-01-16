
class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receive_call(self, name):
        print("Zvonit", name)

    # getter
    def get_number(self):
        return self.number

    # setter
    def set_number(self, new_number):
        self.number = new_number

if __name__ == "__main__":
    p1 = Phone("911", "samsung", 100)
    p2 = Phone("119", "iphone", 200)
    p3 = Phone("191", "xiaomi", 300)

    print(p1.get_number())
    p1.set_number("811")
    print(p1.get_number())