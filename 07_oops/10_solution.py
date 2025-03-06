class Car:
    total_car = 0
    def __init__(self, brand: str, model: str) -> None:
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    def display(self):
        return (f"Car: {self.__brand} {self.__model}")
    
    def get_brand(self):        #general convention to use "get_[attribute]"
        return self.__brand + " !"
    
    #demo polymorphism
    def fuel_type(self) -> str:
        return "Petrol or Diesel"

    @staticmethod
    def general_desc():
        return "Lorem ipsum for car description"
    
    @property
    def model(self) -> str:
        return self.__model
    

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar(Battery, Engine, Car):
    pass


my_tesla = ElectricCar("Tesla", "Model S")

print(my_tesla.battery_info())
print(my_tesla.engine_info())
print(my_tesla.model)