import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choice([2,5,1,0])) # it picks any one of them
print(random.choices([2,5,1,0],k=2))
print(random.choices("Haritha",k=4))
print(",".join(random.choices("Haritha",k=4)))

print(string.ascii_letters)
print(",".join(random.choices(string.ascii_letters+string.ascii_lowercase,k=4)))

li = [1,2,3,4]
random.shuffle(li)
print(li)