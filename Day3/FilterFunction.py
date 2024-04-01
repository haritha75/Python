# based on the condition we can fileter data
items =[
  ("item1",3),
  ("item2",1),
  ("item3",0)
]
x = list(filter(lambda item:item[1]>=1,items))
print(x)