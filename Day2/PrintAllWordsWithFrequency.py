s="this is a word string having many many word"
k=2
words = s.split()
print(words)

d ={}
for word in words:
  if word in d:
    d[word] = d[word]+1 # to mention key we get value and adding one to that value
  else:
    d[word] =1
print(d)    

# another way

d ={}
for word in words:
    d[word] = d.get(word,0)+1 # if key their it return value and adding 1 to that if key is not their  it return none to prevent that we mention zero now zero is the value one will be added to that value

print(d)    

# if given k equal to that value print that word
for i in d:
   if d[i]==k:
      print(i)

# using function      
      
def printFrequenceWord(s,k):
    d={}
    words = s.split()
    for word in words:
      d[word] = d.get(word,0)+1 
    for i in d:
     if d[i]==k:
       print(i)  

  
s="this is a word string having many many word"
k=2
printFrequenceWord(s,k)
