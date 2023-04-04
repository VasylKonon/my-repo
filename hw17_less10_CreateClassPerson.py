class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = None

    def __str__(self):
        return f"{self.name}, {self.age}"

    def add_dog(self, dog):
        self.dog = dog

    def bark(self, dog):
        if not isinstance(dog, Person):
            raise TypeError("Invalid input. Expected Dog instance.")
        if self.dog:
            print(f"{self.dog} bark")
        else:
            print("No dog added yet!")


person1 = Person("John", 30, "Male")
person1.add_dog("Labrador")

person1.bark(person1)
