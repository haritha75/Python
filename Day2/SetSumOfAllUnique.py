a={1,2,3,2,4,3}
print(a)
# it is a set does not allows duplicates
# like i hashset in java
# it is also mutable

a.add(5)
print(a)
print(type(a))
# difference dictironary store key value pari here only key will be stored

# intersting one is  if you print empty set type it gives dictionary

a={}
print(type(a))
# 
s = set()
print(type(s))

def uniqueValueSum(li):
  s = set()
  for i in li:
    s.add(i)
  sum1=0  
  for i in s:
    sum1 +=i
  print(sum1)


uniqueValueSum([1,2,4,1,2,5,2,5,1,4,5])

