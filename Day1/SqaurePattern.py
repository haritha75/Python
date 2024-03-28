n = int(input())

for i in range(1, n + 1): # 1 to 4 and 5 will be excluded
    for j in range(n):
        print(i, end='')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end='')
    print()    

for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end='')
    print()        