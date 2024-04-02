# we have some magic method in python it automatically calls based on situaions

class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
            
    def draw(self):
        print(f"Point ({self.x}, {self.y})")  

point = Point(1,2)    
print(point) # it gives some address we can ovveride this method like this also
print(str(point))

# we create object it contains some method that all are belongs to parent class method str methods also parent class it return address we can ovverride that method

# In Python, the parent class of all classes is the object class. The object class is the base class for all Python classes, 
# and it provides default implementations for various methods like __new__(), __init__(), __del__(), __repr__(), __str__(), etc.

