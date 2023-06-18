class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = None

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"

    def add_dog(self, dog):
        if isinstance(dog, Dog):
            self.dog = dog
        else:
            raise ValueError("Invalid input of dog")

    def bark(self):
        if self.dog is not None:
            self.dog.bark()
        else:
            return f"{self.name} doesn't have a dog."


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"The dog's name is {self.name} and the breed is {self.breed}"


person1 = Person("John", 30, "Male")
dog1 = Dog("Max", "Labrador", 3)
person1.add_dog(dog1)

print(person1)
print(person1.bark())
