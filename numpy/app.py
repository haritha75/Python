import numpy as np
# numpy support all operations on matrixes or arrays
# using numpy we can less code also
# mathematical functions to operate on these arrays efficiently. 

# Create a 2D NumPy array
array = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
print(array)
print(array.shape)

array = np.zeros((2,3),dtype=int)
print(array)
array = np.ones((2,3),dtype=int)
print(array)
array = np.full((2,3),5,dtype=int)
print(array)

array = np.random.random((3,4)) # it creates random values  3 rows and 4 columns
print(array)
print(array[0][1])
print(array[0,1])
print(array>0.3)
print(array[array>0.2])

print(np.sum(array))
print(np.floor(array))
print(np.ceil(array))

array1 = np.array([1,2,3])
array2 = np.array([1,2,3])
print(array1+array2)

# using numpy
dimentional_inch = np.array([1,2,3])
dimentional_cm = dimentional_inch*2.54
print(dimentional_cm)

# using python

dimentional_inch = [1,2,3]
dimentional_cm = [x*2.54 for x in dimentional_inch]
print(dimentional_cm)