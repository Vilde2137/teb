import math
class Shape:
    def area(self):
        raise NotImplementedError(" ")

    def perimeter(self):
        raise NotImplementedError(" ")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.height = height
        self.area()
        self.checkIfCorrect()

        def checkIfCorrect(self):
            if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.c + self.b <= self.a):
                raise ValueError("Triangle has incorrect coordinates.")

        def area(self):
            s = (self.a + self.b + self.c) / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        def perimeter(self):
            return self.a + self.b + self.c



