# we can represent in three ways
# string nothing but sequence of characters internally it stpre sequences of unicodes

str11 = "abc"
str1='abc'
str3='''abc
def''' # it is allows multi lines also
print(str3[2+1]) # it represent new line or space because it start new line right
print(str11[-1]) # string also allows negative indexing
print(str3)

# String are like variables means immutable when store one value and another variables store same data then that vairable pointing to same vairable if assign new value new  storage will be created means reference will be pointing new value

a = "haritha"
c="haritha"
print(id(c))
print(id(a))
c="hari"
print(id(c))
# if have same content then they poingint to tsame refernce only if you have new one then reference will be  changed
#c[0]='a' # we cannot do like this because string are immutable  but list we can do when try to do add to the new string then it will create new value and reference will be changed
# if you want changed it will effect to the other vairbales because other variable pointing to the same reference right so original value not changed new value will be created that refence poingint to the new addres
print(a)

# Concatination in two ways
# 1)
a="red"
print(id(a))
a = a+"blue"
print(id(a))
a+"blue"+"green"
print(id(a))
# 2)
print(a*3)
# when try add new string  to the already exisitng one new value will be created and refernce also changed
#print(a+3) # we cannot add integer to the string but java it allows
a="green"
a =a+str(3) # typecast
print(a)

# silicing same like list

str12 = "Haritha"
print(str12[1:4])
print(str12[:5:2])
print(str12[-1]) #negative index
print(str12[:2:-1]) # means start with 6:2:-1
print(str12[-5:-3])
print(str12[5:2:-2])

# Iteration on string

str3 ="Hello World"

for i in range(len(str3)):
  print(str3[i],end='')

  # another way
  count=0
for ele in str3:
  print(ele,end='')  
  if(ele=='l'):
    count +=1
print()    
print(count)    

# substring is nothing continuous part of string
str4="Hello"


if 'ell' in str4:
  print("Yes contains")
else:
  print("not contains")  


for i in  range(len(str4)):
  print(str4[0:i+1])

