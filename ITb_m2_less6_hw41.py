class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        return f"Color: {self.color}"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def display_color(self):
        return f"Color: {self.color}."


class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, width=side_length, height=side_length)
        self.side_length = side_length


square = Square("Green", 8)
print(square.display_color())
print(square.width)
print(square.height)
print(square.side_length)
