# Class Method (using @classmethod decorator): These methods are bound to the class itself rather than the instances. 
# They can access class-level variables and can be called using the class name.
class Example:
    # Class variable
    class_variable = 0

    def __init__(self, instance_variable):
        # Instance variable
        self.instance_variable = instance_variable

    # Class method
    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print("Class variable value:", cls.class_variable)

    # Instance method
    def instance_method(self):
        print("This is an instance method.")
        print("Instance variable value:", self.instance_variable)
        print("Class variable value:", self.class_variable)

# Calling the class method
Example.class_method()

# Creating an instance of Example class
obj = Example(10)

# Calling the instance method
obj.instance_method()


# another one cla means class name reference

class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0) # it means Point(0,0) means we are passing tothe constrctor
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")  

point = Point.zero()
print(point)        

        
point.draw()        