class Vehicle:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price

    def __gt__(self, other):
        return self.speed > other.speed

    def __str__(self):
        return f"{self.name} has speed {self.speed}km/h and cost {self.price}$"

    def __repr__(self):
        return f"|Name: {self.name}, speed: {self.speed}, price: {self.price}|"

    @staticmethod
    def sorted_speed():
        sorted_list = sorted(vehicles, key=lambda x: x.speed)
        return sorted_list


vehicles = [
    Vehicle("Car", 240, 50000),
    Vehicle("Airplane", 500, 1000000),
    Vehicle("Motorcycle", 350, 15000)
]

print(vehicles[1] > vehicles[0])
print(vehicles)
sorted_vehicles = Vehicle.sorted_speed()
print(sorted_vehicles)
for i in sorted_vehicles:
    print(i)
