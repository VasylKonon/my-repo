class Student:
    def __init__(self, name, surname, grades_list):
        self.name = name
        self.surname = surname
        self.grades_list = grades_list

    def __str__(self):
        return f"Name: {self.name}, surname: {self.surname}, " \
               f"number of grades: {len(self.grades_list)} {self.grades_list}"

    def __len__(self):
        return len(self.grades_list)

    @staticmethod
    def sorted_by_len_scores():
        len_scores = sorted(students, key=lambda x: len(x))
        return len_scores


students = [
    Student("Vasyl", "Kononenko", [4, 4, 4, 4]),
    Student("Anton", "Antonovich", [5, 5, 5]),
    Student("Max", "Max", [4, 5, 4, 5, 3, 2])
]

sorted_students = Student.sorted_by_len_scores()
for student in sorted_students:
    print(student)
