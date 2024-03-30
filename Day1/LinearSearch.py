li = [int(x) for x in input().split()]
print(li)
ele = int(input())
for i in range(len(li)):
  if(li[i]==ele):
    print(i)
    break
else:
  print(-1)  

# linear search through function

def linearSearch(li,ele):
  for i in range(len(li)):
    if(li[i]==ele):
      return i    
  else:
    return -1

li = [1,2,5,7,8]
index = linearSearch(li,7)
print(index)