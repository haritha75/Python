# li = [int(x) for x in input().split()]
def binarySearch(li,ele):
  start =0
  end = len(arr)-1
  while(start<=end):
    mid = (start+end)//2
    if(arr[mid]==ele):
      return mid
    elif arr[mid]<ele:
      start = mid+1
    else:
      end = mid-1
  return -1      

arr = [1,3,5,6,7,8]
index = binarySearch(arr,5)
print(index)