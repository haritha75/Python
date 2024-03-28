n = int(input("Enter number of rows : "))

for i in range(n):
  for j in range(n):
    print("*",end='')
  print()  



  # using while loop

k=1
while k<=n:
    m=1
    while m<=n:
      print("*",end='')
      m = m+1
    print()
    k = k+1    
