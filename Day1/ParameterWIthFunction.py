def f(a,b,c=0):
  print(c)
  return a+b+c
print(f(2,3,5))
print(f(2,3))

# by deault end value is new line like this end='\n'

def f1(a=0,b,c): # it does not work becuase first we have to mention non default value after default values like this (b,c,a=0)
  return a+b+c;

def f2(a,b,c=2,d=1):
  return a+b+c+d

print(f2(1,2))
print(f2(a=1,b=3)) # also mention value like this also
print(f2(1,4,c=3))
print(f2(2,5,d=6))
print(f2(b=1)) # it dpes not because we are not mention a value
print(f2(b=1,a=5)) # it does not matter position of emntioning values