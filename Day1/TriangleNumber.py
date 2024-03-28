n = int(input())

for i in range (1,n+1):
  for j in range (1,n+1-i):
    print(" ",end='')
  b=i
  for k in range(1,i+1):
    print(b,end='')
    b = b+1
  f = b-2  
  for h in range(1,i):
    print(f,end='')
    f = f-1  
  print()    