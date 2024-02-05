class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x,self.y)
    
    def move(self,x1,y1):
        self.xo = self.x
        self.yo = self.y
        self.x = x1
        self.y = y1
        
     
    def dist(self):
        return (abs(self.xo - self.x),abs(self.yo - self.y))
    

x1 = int(input())
y1 = int(input())
point = Point(x1, y1)

point.show()

x2 = int(input())
y2 = int(input())

point.move(x2, y2)

point.show()

print(point.dist())