n = int(input())

for i in range(1,n+1):
  for j in range(1,n+1-i):
    print(" ",end='')
  for k in range(1,i+1):
    print(k,end='')
  for m in range(1,i):
    print(k-1,end="")  
    k =  k-1
  print()    