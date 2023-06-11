class Rectangle:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

    def square(self):
        return f"The square is {self.first_side * self.second_side}"

    def perimetr(self):
        return f"The perimetr is {(self.first_side + self.second_side) * 2}"


rectangle = Rectangle(8, 10)
print(rectangle.square())
print(rectangle.perimetr())

