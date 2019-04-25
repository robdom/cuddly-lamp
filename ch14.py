# CLASS VARIABLES

# class Rectangle():
#     recs = []

#     def __init__(self, w, l):
#         self.width = w
#         self.len = l
#         self.recs.append((self.width, self.len))

#     def print_size(self):
#         print("""{} by {}""".format(self.width, self.len))

# r1 = Rectangle(10, 24)
# r2 = Rectangle(20, 40)
# r3 = Rectangle(100, 200)

# print(Rectangle.recs)

# CHALLENGES 1-2

class Square():

    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append((self.s1, ))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

square1 = Square(5)

print(Square.square_list)

print(square1.s1)

print(square1)

# CHALLENGE 3

square2 = Square(6)

square3 = square2

square6 = Square(6)

def isSame(obj1, obj2):
    if obj1 is obj2:
        return True
    else:
        return False

    # can just say: return obj1 is obj2

print(isSame(square2, square3))

print(isSame(square2, square6))

print(isSame(square3, square6))



