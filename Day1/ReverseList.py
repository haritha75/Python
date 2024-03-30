# using swap logic
def reverse(li):
  for i in range(len(li)//2):
    temp = li[i]
    li[i] = li[len(li) - i - 1]
    li[len(li) - i - 1] = temp

li = [1,2,3,4,5]
reverse(li)
print(li)

# using backwards
def rev(li):
  rev_list=[]
  for i in range(len(li)):
    rev_list.append(li[len(li)-i-1])
  return rev_list
li=[1,2,3,4,5]
li = rev(li) 
print(li)   
