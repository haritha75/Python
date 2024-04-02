# a class can inherit attributes and methods from more than one parent class. This allows for a high degree of flexibility in designing class relationships.

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Animal eats")

class Flyable:
    def eat(self):
        print("flying")

 

class Bird(Animal, Flyable):  # Multiple inheritance
   pass

# Create an instance of Bird
bird = Bird()

bird.eat() # first it look for the bird class if not their and loop first parameter class if not their next class
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Animal eats")

class Flyable:
    def eat(self):
        print("flying")

 

class Bird(Flyable,Animal):  # Multiple inheritance
   pass

# Create an instance of Bird
bird = Bird()

bird.eat() 
# if not use properly it is bad thing if use good manner it is good manner
