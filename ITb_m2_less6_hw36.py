class Person:
    def __init__(self):
        self.__name = None
        self.__age = None

    def set_name(self, name):
        if not any(map(str.isdigit, name)):
            self.__name = name
        else:
            print("Error")

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age < 0 or age > 120:
            print("Error")
        else:
            self.__age = age

    def get_age(self):
        return self.__age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())
print(person.get_age())

person.set_name("John121")
print(person.get_name())
