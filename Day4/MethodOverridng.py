# replacing content with same method in sub class
class Animal:
    def __init__(self):
        self.age = 1
        print(self.age)


    def eat(self):
        print("eat")

class Mammal(Animal):
    def eat(self):  # Method overriding
        super().__init__() # if you want call super class properties and method use super keyword
        print("not eat")

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()  

class Animal:
    def __init__(self):
        self.age = 1
        print('calling parent class constrctor')


    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight=22
        print(self.weight)

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()

