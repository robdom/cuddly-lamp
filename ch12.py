# CHALLENGE 1

class Apple():
  def __init__(self, color, weight, kind, organic):
    self.color = color
    self.weight = weight
    self.kind = kind
    self.organic = organic

# CHALLENGE 2

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

circle1 = Circle(5)

print(circle1.area())

# CHALLENGE 3

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

triangle1 = Triangle(3, 8)

print(triangle1.area())

# CHALLENGE 4

class Hexagon():
    def __init__(self, side1, side2, side3, side4, side5, side6):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hex1 = Hexagon(2, 5, 6, 7, 3, 9)

print(hex1.perimeter())


