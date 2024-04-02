class Point:
  def draw(self):
    print("draw")

# The line point = Point() is simply creating an instance of the Point class. 
point = Point() # it is a object
print(type(point))
print(isinstance(point,Point))
point.draw()

# t represents the instance of the class itself. 
# When you call a method on an instance of a class, Python automatically passes the instance as the first argument to the method.