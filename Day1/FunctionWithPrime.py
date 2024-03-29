def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        return True
    return False

def PrimeFromToN(n):
    for i in range(2, n + 1):
        isPrimeOrNot = isPrime(i)
        if isPrimeOrNot:
            print(i)

n = int(input("Enter a number: "))
PrimeFromToN(n)
