class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def draw(self):
    print(f"Point ({self.x}, {self.y})")  

point = Point(1,2)
point.draw()    
print(point.x)

# in python we have magical methods inti also one of the magical method it is constrctour
# in a class if you have methods then it contains atleast one parameter called self it is pointingcuurent object like this keyword in java
# we donot nee to give self value to the argument python automatically gives
# In Python, the __init__ method serves as a constructor for a class. 
# It is automatically called when you create a new instance of the class. This method is where you can initialize the attributes of the instance.

# after we create object we can declare attributes because objects are in python are dynamic

point.z = 12
print(point.z)


