class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.__brand = brand
        self.model = model
    def display(self):
        return (f"Car: {self.__brand} {self.model}")
    
    def get_brand(self):        #general convention to use "get_[attribute]"
        return self.__brand + " !"
    
    #demo polymorphism
    def fuel_type(self) -> str:
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__(self, brand: str, model : str, battery_size : str) -> None:
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric"
    


my_car = Car("BMW","M5")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_car.fuel_type())
print(my_tesla.fuel_type())
