import math
from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        raise NotImplemented

    def __str__(self):
        return f"{type(self).__name__}:{self.name}"


class Circle(Figure):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def perimeter(self):
        return math.pi * self.radius * 2

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Figure):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)

    def perimeter(self):
        return (self.width + self.length) * 2

    def square(self):
        return self.width * self.length


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(name)

    def perimeter(self):
        return self.a + self.b + self.c

    def halfper(self):
        return self.perimeter() * 0.5

    def square(self):
        return math.sqrt(self.halfper() * (self.halfper() - self.a) * (self.halfper() - self.b) * (
                self.halfper() - self.c))


if __name__ == '__main__':
    a = Triangle("tria", 3, 4, 5)
    print(a)
