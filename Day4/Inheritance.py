# it is a mechanism we can getting propertie and behavious from one class to another class
class Animal:
  def __init__(self):
    self.age =1
  def eat(self):
    print("eat")

class Mammal(Animal):
  def walk(self):
    print("walk")

class Fish(Animal):
  def swim(self):
    print("swim")

m = Mammal()
m.eat()
print(m.age)
print(isinstance(m,Mammal))
print(isinstance(m,Animal)) # true because mummal inheritance the animal class
# and alos one more importent one is if class not inheritate another method then that method automatically inherite the object class that is the parent class of all other classes and also getting all methods
print(isinstance(m,object))
print(issubclass(Mammal,object))
print(issubclass(Mammal,Animal))