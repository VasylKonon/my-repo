from math import pi


class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        pass

    def perimetr(self):
        pass

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Color: {self.color}"


class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimetr(self):
        return (self.length + self.width) * 2

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Area: {self.area()}\n" \
               f"Perimetr: {self.perimetr()}"


class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimetr(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Area: {self.area()}\n" \
               f"Perimetr: {self.perimetr()}"


class Square(Shape):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimetr(self):
        return self.side * 4

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Area: {self.area()}\n" \
               f"Perimetr: {self.perimetr()}"


rectangle = Rectangle("Rectangle", "Red", 5, 10)
circle = Circle("Circle", "White", 5)
square = Square("Square", "Black", 5)
print(rectangle)
print("=" * 50)
print(circle)
print("=" * 50)
print(square)   
