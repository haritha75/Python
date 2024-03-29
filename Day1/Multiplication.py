n = int(input())
for i in range(n+1):
  if(i%3==0):
    print(i)

a = int(input())
b = int(input())

if a%3==0:
  s = a
elif a%3==1:
  s = a+2
else:
  s =  a+1
for i in range(s,b+1,3):
  print(i)    

  