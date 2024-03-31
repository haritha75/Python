# to store data in n*m manner using two domentional lists
# it is nothing list of list
li = [[1,2,3,4],[5,6,7,8],[11,12,13,14]];
print(li[2][1])

li[2][1] = 22
print(li[2][1])
print(li)
print(li[1])
print(id(li))
print(id(li[0]))
print(id(li[1]))
print(id(li[2]))
# each one have seperate address means reference
# internally it sotre each list in single list only

print(id(li[0][0]))
print(id(li[0][1]))

li[1]="Haritha" # now it will store string then it is not a two d list because list removed and assign to the string then type string only list
print(li)
li[1]=[7,6,4,3] # again it is 2-d list
print(li)

# jagged lists -- if your 2d lists does not have same column length then it is called jagged list

li=[[1,2,3,4,5],[1,2,3],[2,3],[1]]
print(li)
print(li[1][1])
print(li[0][3])