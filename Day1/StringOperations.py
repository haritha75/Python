# split

str1 ="My name is Haritha"
li = str1.split(" ") # it return list
li1=str1.split(" ",1) # how many time we cant split 
print(li1)
print(li)
# replace
str1 = "Hello Haritha"
str2= str1.replace("Haritha","Raj")
print(str1) # string are immutable so original not changed
print(str2) # new one will be created

str1 = "Haritha Haritha Haritha Hello"
str1 = str1.replace("Haritha","Raj",2) # it means how many values we want change if you mention 2 then two values will be changed
print(str1)


# find

str1 ="My name is Haritha"
index = str1.find("na")
index1 = str1.find("nae")

print(index)
print(index1) # if not it print -1

str1 = "My Name is Haritha Hari"
index = str1.find("Ha",16,22) # between 16 to 24 if ha is their it return that start index
print(index)

# lower and upper
str1 = "Haritha"
print(str1.lower())
print(str1.upper())

# starts with

str1 = "my name is Haritha"
print(str1.startswith("my nama")) # here i am change name to nama then wrong one right it gives false
print(str1.startswith("my na"))
print(str1.startswith("Ha",11,22)) # if 11 index start with Ha it return True
print(str1.startswith("Haa",11,22)) # if 11 index start with Ha it return True

# replace character in string
def replacecharacters(str2,char1,char2):
  str1 =""
  for ele in str2:
    if(ele==char1):
      str1 +=char2
    else:
      str1 +=ele
  return str1      


str1 ="abacada"
str1 = replacecharacters(str1,'a','s')
print(str1)

# count vowels,cosonants and digits
def countStrings(str1):
  v,c,d,s=0,0,0,0
  for char in str1:
    if ((char>='a' and char<='z') or (char>='A' and char<='Z')):
      char = char.lower()
      if (char=='a'or char=='e' or char=='i' or char=='o' or char=='u'):
        v +=1
      else:
        c +=1
    elif (char >='0' and char<='9' ):
      d +=1
    else:
      s +=1    
  return v,c,d,s       

str1 = "harithawho12are457you@tell#$me^/83once"
v,c,d,s=countStrings(str1)
print(v,c,d,s)