# In Python, the property method is used to create properties for class instances. 
# It allows you to define custom behavior for attribute access, such as performing validations or computations when getting or setting the attribute. 
# The property method takes up to four arguments: fget (getter function), fset (setter function), fdel (deleter function), and doc (optional documentation string).

class Product:
  def __init__(self,price):
    self.set_price(price)
  def get_price(self):
    return self.__price
  def set_price(self,value):
    if value <0:
      raise ValueError(" price cannot be negative")
    self.__price = value  
  price = property(get_price,set_price)  

product = Product(50)   
print(product.price) #getter
product.price = 20 #setter
print(product.price)
# property to look normal field but internally it has two  methods called getter and setters

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def area(self):
        return 3.14 * self._radius ** 2

    # Using property method to define a property 'radius'
    radius = property(get_radius, set_radius)

# Creating an instance of Circle
circle = Circle(5)

# Getting the radius using property
print("Radius:", circle.radius)  # Output: Radius: 5

# Setting the radius using property
circle.radius = 7
print("Radius after setting:", circle.radius)  # Output: Radius after setting: 7

# Trying to set an invalid value
try:
    circle.radius = -3
except ValueError as e:
    print(e)  # Output: Radius must be positive

# Calculating the area of the circle
print("Area:", circle.area())  # Output: Area: 153.86


# instead of creating property explicite  we can do another way
#  When you use the @property decorator in Python, it automatically creates a property attribute with the same name as the method. 
# So in your Product class, when you decorate the price method with @property, Python automatically creates a property attribute named price.

class Product:
    def __init__(self, price):
        self.__price = price

    @property  # mention property decorator, when Python sees this, it automatically creates a property attibutes price
    def price(self):
        return self.__price

    @price.setter 
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value  

product = Product(50)   
print(product.price)  # Output: 50 (getter)
product.price = 20    # Output: 20 (setter)
print(product.price)  # Output: 20
