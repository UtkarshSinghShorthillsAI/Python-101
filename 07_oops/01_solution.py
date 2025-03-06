class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

myCar = Car("Toyota","Corolla")
print(myCar.brand)
print(myCar.model)


my_new_car = Car("BMW","M5")
print(my_new_car.model)