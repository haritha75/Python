# sometimes we will get an event a execution of a program that are called exception using try and except block we can handle the exception


try:
    # if you enter character get error because we can convert into int enter number then not getting exception
    x = int(input())
except ValueError as msg:
    print("Exception wil be occurs")
    print(msg)
else:
    print("if exception not occcurs on that only it will excute like  for else type")
print("whether exception occurs or not it will always excute like finally block in java ")

# different exceptions
try:
    # if you enter character get error because we can convert into int enter number then not getting exception
    x = int(input())
    f = 10/x
except ValueError as msg:
    print("Exception wil be occurs")
    print(msg)
except ZeroDivisionError:
    print("you didn't allow zero for division")
else:
    print("if exception not occcurs on that only it will excute like  for else type")
print("whether exception occurs or not it will always excute like finally block in java ")

# we can use single except
try:
    # if you enter character get error because we can convert into int enter number then not getting exception
    x = int(input())
    f = 10/x
# it does comes next except because it caches here only so not come
except (ValueError, ZeroDivisionError):
    print("Exception wil be occurs")
    print(msg)
except ZeroDivisionError:  # it ignores we written above one right
    print("you didn't allow zero for division")
else:
    print("if exception not occcurs on that only it will excute like  for else type")
print("whether exception occurs or not it will always excute like finally block in java ")
# cleaning up

try:
    file = open("hello.py")
    # if you enter character get error because we can convert into int enter number then not getting exception
    x = int(input())
    f = 10/x
# it does comes next except because it caches here only so not come
except (ValueError, ZeroDivisionError):
    print("Exception wil be occurs")
    print(msg)
else:
    print("if exception not occcurs on that only it will excute like  for else type")
finally:
    file.close()
    # it does not matter whether exception occurs or not it always excutes

# without finally block you can cleanup activies using with statement
# when using the with statement in Python to handle file operations,
    #  the file is automatically closed after the block of code within the with statement is executed or if an exception occurs within that block.


try:
    with open("Array.py") as file:
        print("file will be opened and also automatically closed using with statement")
    # if you enter character get error because we can convert into int enter number then not getting exception
    x = int(input())
    f = 10/x
# it does comes next except because it caches here only so not come
except (ValueError, ZeroDivisionError):
    print("Exception wil be occurs")
    print(msg)
else:
    print("if exception not occcurs on that only it will excute like  for else type")

# rising exception but it is not good choice always use try method
# Raising exceptions in Python allows you to indicate that an error or unexpected condition has occurred during the execution of your code. 
# You can raise exceptions using the raise statement.
    
def cal(age):
    if age<=0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age    

try:
    cal(-1)
except ValueError as error:
    print(error)    

