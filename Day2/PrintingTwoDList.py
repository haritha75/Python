li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for i in range(len(li)):
  for j in range(len(li[i])):
    print(li[i][j],end=' ')
  print()  

# without range means index like a for each loop
  
for row in li:
  for ele in row:
    print(ele,end=' ')
  print()    

# here last one not join
print('ab'.join("abcd"))
print("ab".join(["1","2","3","4"]))

# list comprehension

li=[[1,2,3,4],[5,6,7],[1,2]]
for row in li:
  output= " ".join([str(ele) for ele in row]) # element will be integer so convert into string 
  print(output)  