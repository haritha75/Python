from array import array

# Creating an array of integers i is nothing but typecod
int_array = array.array('i', [1, 2, 3, 4, 5])

# Creating an array of floating-point numbers
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])



# Creating an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(int_array[0])  # Output: 1
print(int_array[2])  # Output: 3

# Modifying elements
int_array[1] = 10
print(int_array)  # Output: array('i', [1, 10, 3, 4, 5])

# Performing mathematical operations
# For example, adding a constant to each element
for i in range(len(int_array)):
    int_array[i] += 1
print(int_array)  # Output: array('i', [2, 11, 4, 5, 6])

# we can take multiple values of same type like in java