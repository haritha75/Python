# similar to list but not same
# major differwnt is tuple is immutable list is mutable
# slicing,index are same

a =(2,3)
print(type(a))
# if you try to assign multiple values to same variable then python treated as a tuple

b =1,2,3
print(type(b))

print(b[1:])
#b[1]=2
print(b) # shows error because it is immutable
# we cannot delete single element if you want delete total tuple

# del a
# print(a)

a=(1,2,3)
for ele in a:
  print(ele)

print(1 in a)  

c =a+b # here we are adding all into one tuple
print(c)
print(c[0])

d =(a,b) # here we are taking tuple wise
print(d)
print(d[0][1])

e=a*4 #repeated 4 times
print(e)
print(max(e))
# a2=(1,2,(3,4))
# # we cannot compare tuple and int and also tuple and string
# print(min(a2))
a3 =(1,2.2) #we ccan do like this
print(min(a3))
# list to tuple
li=[1,2,3,4]
print(tuple(li))