class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
    def display(self):
        return (f"Car: {self.brand} {self.model}")
    

class ElectricCar(Car):
    def __init__(self, brand: str, model : str, battery_size : str) -> None:
        super().__init__(brand,model)
        self.battery_size = battery_size


my_car = Car("BMW","M5")

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.model)