# In Python, duck typing is prevalent due to its dynamic nature. 
# Instead of explicitly checking the type of an object, Python code often checks for the presence of certain methods or attributes, 
# and if those are present and behave as expected, the code proceeds without caring about the actual type of the object.

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm not a duck, but I can quack like one!")

def make_it_quack(obj):
    obj.quack()

# Both Duck and Person can be passed to make_it_quack
duck = Duck()
person = Person()

make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm not a duck, but I can quack like one!
# only looks existes of a method or attirbutes not type of object
# it focuses on what objects can do rather than their specific types. 
