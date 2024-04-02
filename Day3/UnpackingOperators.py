# Unpacking operators in Python allow you to expand iterables like lists, tuples, dictionaries, etc., into individual elements or key-value pairs. 
# There are primarily three unpacking operators in Python:

values = list(range(5))
print(values)
values = [*range(5),*"Hello"] # it creates individual elements automatically
print(values)
first=[1,2]
second =[3,4,5]
values = [*first,*range(5),*second,*"Hello"] # it creates individual elements automatically
print(values)

# dictionaries

first = {"x":1}
second={"x":10,"y":2}
combined = {**first,**second,"z":33} # it does not contain duplicate keys if you have it update value that's it
print(combined)