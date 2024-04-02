# Raising exceptions is useful for signaling errors or exceptional conditions in your code, 
# allowing you to handle them gracefully or propagate them up the call stack for higher-level handling.

from timeit import timeit # to repeat that menay time using timeit library

def code1():
    def cal(age):
        if age <= 0:
            raise ValueError("Age cannot be 0 or less.")
        return 10 / age

    try:
        cal(-1)
    except ValueError as error:
        pass

# Measure the execution time of code1
print("first code=",timeit(code1,number=10000)) # after 10000 repeation it shows excution time takes

# another way it is very fast

from timeit import timeit

def code2():
    def cal1(age):
        if age <= 0:
            return None
        return 10 / age

    x = cal1(-1)
    if x == None:
        pass

# Measure the execution time of code2
print("second code =", timeit(code2, number=10000))
