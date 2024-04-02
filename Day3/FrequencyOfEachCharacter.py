from pprint import pprint
sentence = "Hello everyone who are"
dic ={}
for char in sentence:
  if char in dic:
    dic[char] +=1
  else:
    dic[char] =1  
print(dic)    
pprint(dic,width=1) # to print dictionary form use like this word =1 means 1 character frequency means not 11 ,12 only one character
# it is also unorder type
# only list can be sorted

print(sorted(dic.items(),key=lambda kv:kv[1])) # actually it gives key values pair and and sorted does not know how to sorted then give lambda expression based on the value we have to sort the dictionary
print(sorted(dic.items(),key=lambda kv:kv[1],reverse=True)) # actually it gives key values pair and and sorted does not know how to sorted then give lambda expression based on the value we have to sort the dictionary
frequency = sorted(dic.items(),key=lambda kv:kv[1])
print(frequency[0])
print(frequency[0][1])