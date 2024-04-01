li = list("Haritha")
print(li)
li = list(range(20))
print(li)
print(li[::2])
li = ["a","b","c"]
print(li)
li =[[0,1],[1,2]]
print(li[0][0])
zeros = [0]*5
print(zeros)
#  the main difference is that in the first case (first, second, *others = numbers), 
# you are unpacking a list and getting the rest of the items as a list, 
# while in the second case (*more in function parameters), you are collecting extra arguments into a tuple within a function definition.

# unpacking a list 
numbers = [0,1,2,3,4,5,6,7]
first,second,*others=numbers
print(first)
print(others) # it treated as a list

first,*others,last=numbers
print(first)
print(last)

def mul(a,b,*more):
  print(a,b,more)
mul(1,2,3,4,5)  

# enumrate

li=["a","c","c"]
for letter in enumerate(li): # enumrator gives index with value also return like a tuple
  print(letter)
  print(type(letter))
  print(letter[0],letter[1]) # to acess index and value using like this because it returns like tuple

# uplacing list
  
  for index,letter in enumerate(li):
    print(index,letter)

# if you want value with index use enumerate function
    
# remove
    
li=[1,2,3,4,5]
print(li)
li.remove(2) # 2 element will be removed
print(li)
li.pop() #last element removed
print(li)
li.pop(2) # particular index will be removed
print(li)
   
li.clear() # all elementd will be removed from the list
print(li)    
    
li=[1,2,3,4]
del li[1] # paritucular one deleted
print(li)  
# del li # total list removed
# print(li)

    
li =[1,2,3,4,5,2,1,1,1]
print(li.index(2))      # return index
# print(li.index(0)) # given value is not their shows error
if 2 in li:
  print(li.index(2))

print(li.count(1))  
# ascending order
li = [2, 1, 4, 2, 0, 1]
li.sort()
print(li)

# descending order
li.sort(reverse=True)
print(li)

li = [2, 1, 4, 2, 0, 1]
print(sorted(li))
print(sorted(li,reverse=True))



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