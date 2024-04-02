# a class inherits from another class, and then another class inherits from that derived class, forming a hierarchical chain of inheritance.
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

# Create an instance of Dog
dog = Dog()

# Access methods from different levels of inheritance
dog.eat()   # Output: Animal eats
dog.walk()  # Output: Mammal walks
dog.bark()  # Output: Dog barks
