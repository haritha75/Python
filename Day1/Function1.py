n = int(input())
r = int(input())
n_fact = 1
for i in range(1,n+1):
  n_fact = n_fact*i

r_fact = 1
for i in range(1,r+1):
  r_fact = r_fact*i


n_r_fact = 1
for i in range (1,n-r+1):
  n_r_fact = n_r_fact*i

ans = n_fact//(r_fact*n_r_fact)    
print(ans)    

# alsmost same code repeating many times
# so to reduce the code we can use function 
# to avoid repetition of the code
# it is a named block of code when we call it start executing ,reliablity and testability meas testing becomes super easy
def fact(n):
    n_fact = 1
    for i in range(1, n + 1):
        n_fact *= i
    return n_fact

n = int(input("Enter n: "))
r = int(input("Enter r: "))

n_fact = fact(n)
r_fact = fact(r)
n_r_fact = fact(n - r)

ans = n_fact // (r_fact * n_r_fact)
print("Combination (n choose r) is:", ans)

# we can do like this also


def ncr(n,r):
   n_fact = fact(n)
   r_fact = fact(r)
   n_r_fact = fact(n - r)
   ans1 = n_fact // (r_fact * n_r_fact)
   print("Combination (n choose r) is:", ans1)