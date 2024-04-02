# Both languages provide a way to define abstract classes that cannot be instantiated directly and contain abstract methods that must be implemented by concrete subclasses.
from abc import ABC, abstractmethod

# Define an abstract base class ABC is a abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Define concrete subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Create instances and use them
circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

square = Square(4)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())
