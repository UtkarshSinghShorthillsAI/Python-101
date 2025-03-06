class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
    def display(self):
        return (f"Car: {self.brand} {self.model}")
    

my_car = Car("BMW","M5")

print(my_car.display())