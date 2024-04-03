# we can get fro this function list of attributes and methods

from package1.Customer import Hellop
print(dir(Hellop)) # it gives all the methods include magic method and also module contain methods also

print(Hellop.__package__)
print(Hellop.__file__)
print(Hellop.__name__)