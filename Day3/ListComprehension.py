#  we can reduce code suing list comprehension
items =[
  ("item1",3),
  ("item2",1),
  ("item3",0)
]

prices = [item[1]  for item in items] # like map metod
print(prices)

prices = [item for item in items if item[1] >= 1] # like a filter method
print(prices)  # Output: [('item1', 3), ('item2', 1)]
