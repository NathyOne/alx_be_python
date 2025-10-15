import math


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        area = self.length * self.width
        return area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{math.pi*self.radius ** 2}"
