# immutable means we cannot change orignal value in the memory
# if you change the value then original value not removed refernce will be pointing to the new value that's it
# variable in python are immutable because when same variable have assign different value right it dpes not effect  to others
# when try to change new value reference also changed 
a =3
print(3)
print(id(a))
a=4
print(4)
print(id(a))

# list are mutable meeans we can change original also because they are pointing to the same reference

li=[1,2,3,4]
print(li[2])
print(id(li[2]))
li[2] = 7
print(li[2])
print(id(li[2]))

li3=[1,2,3,4]
li2=li3
li2[1]=4
print(li3)
# if two list pointing to the same reference then it effect ot the other one
li3=[1,2,3,4]
li2=li3
li2=[3,3,4]
li2[1]=4
print(li3)
print(li2)
# see here both have different references