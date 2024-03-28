n = int(input())

while n !=6:
  if n >=1 and n<=5:
    a = int(input())
    b = int(input())
  if n ==1:
    print(a+b)  
  if n ==2:
    print(a-b)  
  if n ==3:
    print(a*b)   
  if n ==4:
    print(a//b)        
  if n ==5:
    print(a%b)    
  elif n<1 or n>=6:
    print("Invalid operation")  
  n = int(input())  