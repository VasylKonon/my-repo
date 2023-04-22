class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"The dog's name is {self.name} and the breed is {self.breed}")


dog1 = Dog("Tuzik", "Alabay", 2)
dog1.bark()
