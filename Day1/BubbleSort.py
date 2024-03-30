def bubblesort(arr) :
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [6,4,5,3,2,0]
bubblesort(arr)
print(arr)

# in every round we are putting largest element  at last position