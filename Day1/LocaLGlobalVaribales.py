def f3():
  b3 = 12 # local
  print(b3)
  print(a3)
  print(c3)

a3=10 # gloabl
print(a3)
f3()
c3=20
# here before call how many vairables have that all working but after call varaibles not taken


a4=13
def f4():
  global a4 # if you donot want to use global variable mention like this means a4 will be globally avaibale
  #  means i donot want new vairable i want cahnge value to new so new value will be availble globally
  a4=10
  print(a4)
  print(id(a4))

print(a4)
f4()
print(a4)   # acutall print global one if you mention in above global so it print local
print(id(a4))
