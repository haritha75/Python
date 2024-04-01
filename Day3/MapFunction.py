# map function iterate each item 
# The map() function in Python applies a given function to each item of an iterable (like a list) and returns a map object (an iterator) that yields the results.
items =[
  ("item1",3),
  ("item2",1),
  ("item3",0)
]
prices = []
for item in items:
  prices.append(item[1])
print(prices)  


# using map function

x = list(map(lambda item:item[1],items))
for item in x:
  print(item)