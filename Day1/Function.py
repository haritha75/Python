def incr(a):
  a = a*a
  return a
a=2
print(a)
a=incr(a) #here we assign value so it will change pther wise not because vairable s are immutable
print(a)


def inc(li2):
  li2[0]=li2[0]+2
  return
li=[1,2,3,4,5]
print(li)
inc(li) # without assign also list will be changed because list are mutable and pointing li and li2 same reference so if you change it will effect both
print(li)


def inc(li2):
  li2=[9,0,0]
  return
li=[1,2,3,4,5]
print(li)
inc(li) # without assign also list will be changed because list are mutable but  pointing li and li2 difference reference 
print(li)

def inc(li2):
  li2=[9,0,0]
  return li2
li=[1,2,3,4,5]
print(li)
li=inc(li) # without assign also list will be changed because list are mutable but  pointing li and li2 difference reference but we are returning and storing list so it will changed means new list created
print(li)