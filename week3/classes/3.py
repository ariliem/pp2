from shape import Shape

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Area(self):
        return self.length * self.width

a = int(input())
b = int(input())

rec = Rectangle(a,b)
print(rec.Area())