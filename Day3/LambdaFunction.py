# In Python, a lambda function is a small anonymous function defined using the lambda keyword. 
# Lambda functions can take any number of arguments but can only have one expression. 
# They are often used when you need a simple function for a short period of time and don't want to define a full function using the def keyword.
# sorting items

items =[
  ("item1",3),
  ("item2",1),
  ("item3",0)
]

def sort_item(item):
  return item[1]

items.sort(key=sort_item) # here we are passing another function reference to the sort method
print(items)

# using lambda function
# lambda arguments: expression

items.sort(key=lambda item:item[1])
print(items)