# select minimum element keep at 0th next one like repeat process till all ellement correct positiion

def selectionSort(li):
   for i in range(len(li)-1):
      for j in range(i+1,len(li)):
         if(li[i]>li[j]):
            temp = li[i]
            li[i]=li[j]
            li[j]=temp
      
li = [1,5,3,7,2,6,0]
selectionSort(li)
print(li)

# this one is best in above we are swaping everytime

def selectionSort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[min_index] > li[j]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]

li = [1, 5, 3, 7, 2, 6, 0]
selectionSort(li)
print(li)

#  example li[1], li[3] = li[3], li[1]