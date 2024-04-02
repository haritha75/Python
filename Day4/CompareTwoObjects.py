class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")  
point = Point(1,2)
other = Point(1,2)
print(point==other) # it return false because it compares the address of the object not content so we can use eq magic method


class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y
    def __eq__(self, other) :
        return self.x==other.x and self.y==other.y
            
    def draw(self):
        print(f"Point ({self.x}, {self.y})")  
point = Point(1,2)
other = Point(1,2)
print(point==other)


class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y
    def __eq__(self, other) :
        return self.x==other.x and self.y==other.y
    def __gt__(self, other) :
        return self.x>other.x and self.y>other.y
            
            
    def draw(self):
        print(f"Point ({self.x}, {self.y})")  
point = Point(10,20)
other = Point(1,2)
print(point==other)
print(point>other)
print(point<other) # without creating the lt method it gives correct because we are creater gt method right then python automatically understand what happends if less than it gives the correct one


