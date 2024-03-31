# normal way

li =[1,2,3,4]
li1 =[]
for ele in li:
  li1.append(ele**2) # square
print(li1)  

# list comprehensive using this one we can reduce code  in this code to write norman way takes 5 lines here only one we can write

li1=[ele**2 for ele in li]
print(li1)

li_even=[ele**2 for ele in li if ele%2==0]
print(li_even)

li3 = [3,2,6,8,9,18]

li4 =[ele for ele in li3 if ele%2==0 and ele%3==0]
print(li4)

li4 =[ele for ele in li3 if ele%2==0 if ele%3==0]
print(li4)


# intersection

li1=[1,2,3,4]
li2=[2,5,1,6]

li_intersection =[]

for ele in li1:
  for ele1 in li2:
    if ele==ele1:
      li_intersection.append(ele)
print(li_intersection)      

# using list comprehensive

li_intersection = [ele for ele in li1 for ele1 in li2  if ele==ele1]
print(li_intersection)

# list comprehensive first write output and for loop and conditions
li = [1, 2, 3, 4, 5]
li_com = [ele**2 if ele % 2 == 0 else ele for ele in li]
print(li_com)

s = "Haritha"
li = [ele for ele in s ]
print(li)

# list of list means 2d list

li=["Haritha","Roshan","Raj"]

li_com = [[s for s in ele]  for ele in li]
print(li_com)


# take input form the user using list comprehension

str1 = input().split()  # Enter number of rows and columns separated by space
n, m = int(str1[0]), int(str1[1])

# Create a 2D list by taking input for each row
li = [[int(j) for j in input().split()[:m]] for i in range(n)]
print(li)

# jagged array no need same length of columns in all rows

str1 = input().split() # enter number row and cols

n = int(str1[0])
# Create a 2D list by taking input for each row
li= [[ int(j) for j in input().split()]  for i in range(n)]
print(li)

# # normal form
str1 = input().split()  # Enter number of rows and columns separated by space
n, m = int(str1[0]), int(str1[1])

# Create a 2D list by taking input for each row
li = []
for i in range(n):
    row = input().split()
    row = [int(j) for j in row[:m]]  # Restrict the row to the specified number of columns
    li.append(row)

print(li)


# another way to take input and list comphrehension using formula

str1 = input().split()  # Enter number of rows and columns separated by space
n, m = int(str1[0]), int(str1[1])

b = input().split()  # Enter space-separated elements for the 2D array
print(b)

# Create a 2D array from the input list b using formula
arr = [[int(b[m * i + j]) for j in range(m)] for i in range(n)]
print(arr)

# another pne

str1 = input().split()  # Enter number of rows and columns separated by space
print(str1)
n, m = int(str1[0]), int(str1[1])

b = str1[2:]  # here directly take form above string not input
print(b)

# Create a 2D array from the input list b using formula
arr = [[int(b[m * i + j]) for j in range(m)] for i in range(n)]

print(arr)
