n = int(input())
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end='')
  print()  

for i in range(1,n+1):
  for j in range(i,i+i):
    print(j,end='')
  print()  

k=1          
for i in range(1,n+1):
  for j in range(1,i+1):
    print(k,end='')
    k = k+1 
  print()            