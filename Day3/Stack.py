stack = []

# Adding elements to the stack
stack.append(1)
stack.append(3)
stack.append(2)

# Removing the top element of the stack
stack.pop()

# Printing the stack
print(stack)  # Output: [1, 3]

# Accessing the top element of the stack
print(stack[-1])  # Output: 3

# Checking if the stack is empty
if  stack:
    print("Stack is empty")

# Printing the stack again
print(stack)  # Output: [1, 3]
