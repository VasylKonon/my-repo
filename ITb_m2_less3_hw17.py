class Student:
    number_of_students = 0

    def __init__(self, name):
        self.name = name
        Student.number_of_students += 1

    @classmethod
    def print_number(cls):
        return cls.number_of_students


student1 = Student("Vasyl")
student2 = Student("Anton")
student3 = Student("Vlad")

print(Student.print_number())
