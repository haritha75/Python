n = int(input())

for i in range(1, n + 1):
    ch = 'A'  
    for j in range(1, n + 1):
        print(ch, end='')  
        ch = chr(ord(ch) + 1)   # actuall ord method gives ascill value again convert into the char
    print()


for i in range(n):
    ch = chr(ord('A') + i)  # Start each row with a character incremented by i
    for j in range(n):
        print(ch, end='')
        ch = chr(ord(ch) + 1)  # Increment the character for each column
    print()
