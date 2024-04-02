# one action performs many forms
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphism through method overriding
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Different output based on the object type

# same method can exhibit different behavior based on the number of arguments it receives. 
    
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of MathOperations
math_ops = MathOperations()

# Test different method calls
print(math_ops.add(2))          # Output: 2
print(math_ops.add(2, 3))       # Output: 5
print(math_ops.add(2, 3, 4))    # Output: 9


# defining multiple methods with the same name within a class will only keep the last defined method. 
# Therefore, the add method in your MethodOverLoading class will only accept three arguments (a, b, and c), and 
# the previous add methods with fewer arguments will be overridden  and not accessible.
# If you want to achieve a similar functionality to method overloading in Python, 
# you can use default parameter values or variable-length argument lists, as shown in the previous examples.


class MethodOverLoading:
    def add(self,a):
        return a
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=2):
        return a+b+c
    
m = MethodOverLoading()
print(m.add(2,3))
