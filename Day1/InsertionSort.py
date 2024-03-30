#  we are diving two parts one is sort and unsorted parts
def insertionSort(arr):
  for i in range(1,len(arr)):
    j = i-1
    key = arr[i]
    while(j>=0 and arr[j]>key):
      arr[j+1]=arr[j]
      j=j-1
    arr[j+1]=key  
    
arr = [5,3,7,8,1]
insertionSort(arr)
print(arr)