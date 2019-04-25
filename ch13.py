# CHALLENGE 1

# My Implementation

class Rectangle():
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4


class Square():
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4

rectangle1 = Rectangle(2, 4, 2, 4)
print(rectangle1.calculate_perimeter())

square1 = Square(5, 5, 5, 5)
print(square1.calculate_perimeter())

# Cory's Solution

class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter()

# CHALLENGE 2

# My Implementation

class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_side(self, change)
        self.side += change

# Cory's Solution

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 = new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)

# CHALLENGE 3

# My Implementation

class Shape():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):

    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)

class Square(Shape):

    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)

square2 = Square(4, 4)
print(square2.what_am_i())

# Cory's Solution

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()

# CHALLENGE 4

# My Implementation

class Horse():
    def __init__(self, name, age, rider):
        self.name = name
        self.age = age
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rider1 = Rider("Laffit Pincay Jr.")

horse1 = Horse("Swale", 3, rider1)

print(horse1.rider.name)

# Cory's solution

class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

harry_the_horse = Horse("Harry")
the_rider = Rider("Sally", harry_the_horse)

print(the_rider.horse.name)

