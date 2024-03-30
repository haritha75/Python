str = input()
print(str) #it gives string if you enter like this 1 2 3 4 5 then it will be like this '1 2 3 4 5'
str1 = str.split(' ')
print(str1) # ['1', '2', '3', '4', '5']

str = input()
print(str) #it gives string if you enter like this 1,2,3,4,5 then it will be like this '1,2,3,4,5'
str1 = str.split(',')
print(str1) # ['1', '2', '3', '4', '5']

str = input() # 1 2 3 4 5
str1 = str.split() # it automatically split spaces
print(str1)
li = []
for i in str1:
  li.append(int(i))
print(li)  


# another way in single line

li = [int(x) for x in input().split()]
for i in li:
  print(i)