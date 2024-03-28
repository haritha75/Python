n = int(input("enter a number: "))
d = 2
flag = False
while d<n:
  if n%d==0:
    flag = True
    break
  else:
    d +=1

if flag:
  print("Not Prime")
else:
  print("Prime")  

# print 2 to n prime numbers
n1 = int(input())  
k =2
while k <= n1:
  d1=2
  flag1 = False
  while d1<k:
    if k%d1==0:
      flag1 = True
      break
    else:
      d1 +=1
  if (flag1==False):
    print(k)
  k +=1

