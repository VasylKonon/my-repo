class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Sedan(Car):
    def __init__(self, brand, model, doors_number):
        super().__init__(brand, model)
        self.doors_number = doors_number

    def display_info(self):
        return f"Brand: {self.brand} {self.model}\n" \
               f"Number of doors: {self.doors_number}"


class Suv(Car):
    def __init__(self, brand, model, seats_number):
        super().__init__(brand, model)
        self.seats_number = seats_number

    def display_info(self):
        return f"Brand: {self.brand} {self.model}\n" \
               f"Number of seats: {self.seats_number}"


class SportsCar(Car):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def display_info(self):
        return f"Brand: {self.brand} {self.model}\n" \
               f"Max speed: {self.max_speed}"


sedan = Sedan("Toyota", "Camry", 4)
suv = Suv("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

print(sedan.display_info())
print("-------------------------")
print(suv.display_info())
print("-------------------------")
print(sports_car.display_info())
