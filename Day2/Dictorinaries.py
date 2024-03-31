# Dictionaries in Python are used to map unique keys to values efficiently. They're versatile, 
# allowing quick retrieval, manipulation, and storage of related data. 
# They're commonly used for storing settings, configurations, and data where fast lookup by a unique identifier is required.

# this are mutable
#  also very fast that's dictionaries are used
a={}
print(type(a))
a={"haritha":1,1:3.4,6:"hari","hello":1,"hello":2,2:3.4}
print(a)
# it is like a hash map in java it does not allow duplicate keys but allows values
print(len(a))
b= a.copy()
print(b)

c =dict([("the",3),("hari",1),("hi",0)])
print(c)
# here we are passing only keys defautly values are None
c=dict.fromkeys(["abc",7,1])
print(c)
c=dict.fromkeys(["abc",7,1],10) # then all values become 10
print(c)

# getting value using key

a ={"haritha":1,"list":[1,2],"dict":{3,5}}
print(a["haritha"]) # to get value we have to mention key
print(a.get("list"))

print(a.get(2)) # if given key not their it return none
# if given key not theri default it print none if you donot want like that use like this
d = a.get(2,1)
print(d)
print(a.get("li",0))
print(a.get("list",0))

print(a.keys())
print(a.values())
print(a.items()) # it return pairs it nothing but list of tuples

# iteration
a={1:"hari",2:3.4,"hi":4}
for i in a: # it gives only key
  print(i,a[i]) # using key we are print value also

for i in a.values(): # only values
  print(i)

print("hi" in a)   # it tell key in the a or not it checks only key

# adding data to the dictorinary
a={1:"hari",3.4:2,"hi":22}

a["ball"] = (1,2,3)
a["doll"] = {2,3,5}

print(a)
a[1]=111 # here i am update the data which key is 1
print(a)

# update if upu have duplicate key then it update that value if does not duplicate key then it added to the dictionary

a = {1:22,2:54,"hi":33}
b={"hi":12,"hee":100}
a.update(b)
print(a)
# remove data

a.pop(2) # we have to mention key
print(a)
#print(a.pop(100)) # if key is not thie shows error
del a[1]
print(a) # same above like
a.clear() # it just clear all key value pari not dictionary
print(a)
del a # it delete total dictionary
print(a)

