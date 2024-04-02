class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __eq__(self,other):
    return self.x==other.x and self.y==other.y  
  
p1 = Point(1,2)
p2=Point(1,2)
print(p1==p2)  

# another way using data memebers
# collections.namedtuple is a factory function for creating tuple subclasses with named fields.
#  It provides an easy way to create simple classes without having to write a full class definition manually.

from collections import namedtuple

# Define a named tuple type called 'Point' with two fields: 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

# Create instances of the Point class
p1 = Point(1, 2)
p2 = Point(1, 2)

# Access fields using named attributes
print(p1.x, p1.y)  # Output: 1 2
print(p2.x, p2.y)  # Output: 3 4

# Access fields using index
print(p1[0], p1[1])  # Output: 1 2
print(p2[0], p2[1])  # Output: 3 4
print(p1==p2)  
