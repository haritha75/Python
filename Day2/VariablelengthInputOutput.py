def var(a,b,*more):
  print(a)
  print(b)
  print(more)
  print(type(more))
  ans = a+b
  for i in more:
    ans +=i
  return ans    

val = var(2,3,5,6,7)
print(val)
#  what happends if you enter more than required paramter then it takes tuple but must and should mention required parameteer value

def sundiff(a,b):
  return a+b,a-b,a*b

c = sundiff(2,3)
print(c) # it returns tuple because function return two values to the same variable then python consider it is tuple

c,d =sundiff(2,3) # now here we are mention seperate variables right then it takes noramlly
print(c)
print(d)

def sundiff(a,b):
  return a+b,a-b,a*b

c,d = sundiff(1,2) # it gives error because function return 3 values but we have two right so it gives error on that time take one vairbale it consider tuple other wise take mention variables
print(c)
