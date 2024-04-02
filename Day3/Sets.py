#  it is nothing but unorder collection of ellements contains unique values only
# sets are not sequencial order means unordered  so we cannot access using indexes like hashset in java

set1 = {1,2,3,2,1}
print(set1)

set1 = {} # it default return dictionary
print(type(set1))

# we can suse like this

set1 =  set()
print(type(set1))
set1.add(4)
set1.add(1)
set1.add(9)
set1.remove(1)
print(set1)


set1 ={1,2}
set2 = {3,4,1}
print(set1 | set2) # union
print(set1 & set2) # intersection
print(set1-set2) # set2 not contains values in set1
print(set1^set2) #either of one set value but not both set value means not interesection value

if 1 in set1:
  print("yes")