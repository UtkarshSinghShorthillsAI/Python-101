# A static method is a method that belongs to the Class rather than the instance of a Class.

class Car:
    total_car = 0
    def __init__(self, brand: str, model: str) -> None:
        self.__brand = brand
        self.model = model
        Car.total_car += 1
    def display(self):
        return (f"Car: {self.__brand} {self.model}")
    
    def get_brand(self):        #general convention to use "get_[attribute]"
        return self.__brand + " !"
    
    #demo polymorphism
    def fuel_type(self) -> str:
        return "Petrol or Diesel"

    @staticmethod
    def general_desc():
        return "Lorem ipsum for car description"
    

class ElectricCar(Car):
    def __init__(self, brand: str, model : str, battery_size : str) -> None:
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric"
    


my_car = Car("BMW","M5")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print("Desc: ", my_car.general_desc()) # This should not give the description
print("Desc: ", Car.general_desc())