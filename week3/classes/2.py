class Shape:
    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def Area(self):
        return self.length * self.length
    
Shape1 = Shape()
print(Shape1.Area())

length = int(input())
Square1 = Square(length)

print(Square1.Area())