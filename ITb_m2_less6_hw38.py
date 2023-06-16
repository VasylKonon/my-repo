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


shape = Shape("Red")
print(shape.display_color())

