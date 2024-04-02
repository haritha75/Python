class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    
point = Point(10,20)
other = Point(1,2)
combined = point + other

print(combined.x)    
            
#  when you do combined = point + other, it's calling the __add__ method of the point object (point.__add__(other)), passing other as an argument. 
# This returns a new Point object with x coordinate being the sum of point.x and other.x, and y coordinate being the sum of point.y and other.y.

