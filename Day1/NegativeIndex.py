li = [1,2,3,4,5]
print(li[-1])
print(li[-2])


for i in range(len(li)-1,-1,-1):
  print(li[i])

# for i in range(-1,len(li),1):
#   print(li[i])  
  
# sequence in list  
  
print(li[1:4:2]) # start ,end  and step
print(li[1:])
print(li[1::2]) # strt willbe 1 and end by default end of the list and step is 2
print(li[:3]) # start default 0 and end will be 3 and step is 1
print(li[-1:])
print(li[-3:-1])


n = int(input("Enter the number of elements: ")) # Taking input for the number of elements

li1 = [] # Creating an empty list to store string or character values
li2 = [] # Creating an empty list to store integer values

# Loop to input values for both lists
for i in range(n):
    li1.append(input("Enter a string or character value: ")) # Appending string or character values to li1
    li2.append(int(input("Enter an integer value: "))) # Appending integer values to li2

# Printing the contents of both lists
print("List of strings or characters:", li1)
print("List of integers:", li2)
