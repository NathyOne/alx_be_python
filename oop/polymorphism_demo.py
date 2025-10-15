import math


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return f"The area of the Rectangle is {self.width*self.length}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"the area of the circle {math.pi*self.radius ** 2}"
