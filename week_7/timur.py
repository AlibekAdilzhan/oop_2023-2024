from dataclasses import dataclass

@dataclass
class Film:
    name: str
    Director: str
    year: int
    cash: float

    def set_name(self, new_name: str):
        self.name = new_name
    
    def get_director(self):
        return self.Director
    
    def get_cash(self):
        return self.cash
    
    def __int__(self):
        return self.cash + 100

    def set_new_cash(self, new_cash: float):
        self.cash = new_cash


f1 = Film("asdf", "adf", 2001, 1500)
print(int(f1))

