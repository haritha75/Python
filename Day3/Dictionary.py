def save(**more):
  print(more)

save(a=1,b=2,c=3,d=4,f=5)  

def save(a,b,**more):
  print(a,b,more)

save(a=1,b=2,c=3,d=4,f=5)  

def save(a,b,**more):
  print(a,b,more)

save(1,2,c=3,d=4,f=5)  

# here it tkakes remaning dictionary we are mentioning ** like this so we have to pass keys also
# def save(a,b,**more):
#   print(a,b,more)

# save(1,2,3,4,5)   # we are not passingkeys so ti shows error

def incre(number,by):
  return number+by
print(incre(1,by=2))