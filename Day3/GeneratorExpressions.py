from sys import getsizeof
values = (x*2 for x in range(10000))
print(values) # it gives generator object whenuse open brackets type
#  we cannot read value directly use iterator type like for loop
for i in values:
  print(i)
 
# print(len(values)) # it gives error because it is object right it does not have size
  print("gen: it takes less bytes because it does not store all values in memroy",getsizeof(values))

values = [x*2 for x in range(10000)]
print(values) # see here it gives all the values
print("size of list",getsizeof(values))
# compare to list generator object takes less 