class Animal:
    def __init__(self, animal_name, animal_type):
        self.animal_name = animal_name
        self.animal_type = animal_type

    def display_info(self):
        return (f"Name: {self.animal_name}\n"
                f"Type: {self.animal_type}")


class Mammal(Animal):
    def __init__(self, animal_name, animal_type, food_type):
        super().__init__(animal_name, animal_type)
        self.food_type = food_type

    def display_info(self):
        return (f"Name: {self.animal_name}\n"
                f"Type: {self.animal_type}\n"
                f"Food type: {self.food_type}")


class Carnivore(Mammal):
    def __init__(self, animal_name, animal_type, food_type, num_teeth):
        super().__init__(animal_name, animal_type, food_type)
        self.num_teeth = num_teeth

    def display_info(self):
        return (f"Name: {self.animal_name}\n"
                f"Type: {self.animal_type}\n"
                f"Food type: {self.food_type}\n"
                f"Number of teeth: {self.num_teeth}")


class Lion(Carnivore):
    def __init__(self, animal_name, animal_type, food_type, num_teeth, mane_size):
        super().__init__(animal_name, animal_type, food_type, num_teeth)
        self.mane_size = mane_size

    def display_info(self):
        return (f"Name: {self.animal_name}\n"
                f"Type: {self.animal_type}\n"
                f"Food type: {self.food_type}\n"
                f"Number of teeth: {self.num_teeth}\n"
                f"Mane size: {self.mane_size}")


lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Mufasa", "Tiger", "Carnivore", 40)
mammal = Mammal("Max", "Elephant", "Herbivore")

print(lion.display_info())
print("-------------------------")
print(carnivore.display_info())
print("-------------------------")
print(mammal.display_info())
