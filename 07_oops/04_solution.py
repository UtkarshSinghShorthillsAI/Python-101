class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.__brand = brand
        self.model = model
    def display(self):
        return (f"Car: {self.__brand} {self.model}")
    
    def get_brand(self):        #general convention to use "get_[attribute]"
        return self.__brand + " !"
    

class ElectricCar(Car):
    def __init__(self, brand: str, model : str, battery_size : str) -> None:
        super().__init__(brand,model)
        self.battery_size = battery_size
    

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(my_tesla.__brand)
print(my_tesla.get_brand() )