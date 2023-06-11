from math import pi


class Circle:
    number_pi = pi

    def __init__(self, r):
        self.r = r

    def find_square(self):
        square = Circle.number_pi * (self.r ** 2)
        return square

    def find_length(self):
        length = 2 * Circle.number_pi * self.r
        return length

    def __str__(self):
        return f"The square of circle is {self.find_square()} and the length of circle is {self.find_length()}"


circle = Circle(5)
print(circle)
