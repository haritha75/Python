# list
# normal way
list1=[]
for i in range(5):
  list1.append(i)
print(list1)  
# list compresion
list1 = [i for i in range(5)]
print(list1)

# sets

# normal way
set1 = set()
for i in range(5):
  set1.add(i)
print(set1)  

# set compresion

set1  ={i for i in range(5)}
print(set1)

# dictironary 
# normal way'
dic = {}
for i in range(5):
  dic[i] = i*2
print(dic)  

# dict compreshion

dic={i:i*2 for i in range(5)}
print(dic)


# Tuples cannot be directly created using list comprehensions. 
# List comprehensions are specifically designed for creating lists. However, you can use a generator expression to create a tuple. Here's an example:
tuple_example = tuple(x for x in range(5))
print(tuple_example)

tuple1 = (x for x in range(5))
print(tuple1) # it gives some  generator object we cannot get direct value if you want convert tuple otherwise use for loop for iteration

tuple1 = tuple(x for x in range(5))
print(tuple1) # it gives some object so we have to convert tuple
