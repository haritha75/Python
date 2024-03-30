#  it can store multiple values of hetrogenous values at a time it is dynamical size index size with 0

li = []
print(type(li))
li = [1,2,3,"Haritha",3.4]
print(type(li))
print(li[3]) # using index we can access elmenent in list
li[0]=5
print(li[0])
# slicing

print(li[2:4]) # 4 will be excluded
print(li[1:])
li.append("hello")
li.insert(1,"222")
print(li[0:])
print(li)
li.append([6,7,8]) # it insert like insize another list
print(li)
li.extend([11,12,13]) # it insert like normally
print(li)

li.remove(11) # it remove mentioning elelment from the list not position
print(li)
li.pop() # it remove last element
print(li)
li.pop(4) # it remove pariticular index
print(li)
print("Size of the list:", len(li))


# list actually stores references of elements
# references are stored contignously
# list will be resize when try to add new element means double the size new list will be created and previous references copies and also new one added to the list


for i in range(len(li)):
  print(li[i])

for ele in li: #like for each loop
  print(ele)  # without index

for  ele in li[2:]:
     print(ele)

for ele in li[2:4]:
  print(ele)