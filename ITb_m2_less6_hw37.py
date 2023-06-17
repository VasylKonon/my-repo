class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, mileage):
        if mileage + self.mileage > 300000:
            print("You reach the limit")
        else:
            self.mileage += mileage


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car.get_mileage())

car.drive(100)
print(car.get_mileage())

car.drive(10000000)
print(car.get_mileage())
