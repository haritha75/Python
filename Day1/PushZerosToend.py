def pushToZerosend(arr):
    zeros = 0
    arr1 = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        else:
            arr1.append(arr[i]) 
    for i in range(zeros):
        arr1.append(0)  
    return arr1

arr = [0, 1, 0, 2, 0, 1, 0]
arr = pushToZerosend(arr)
print(arr)
