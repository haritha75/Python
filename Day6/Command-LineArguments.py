import sys
print(sys.argv) # it return array  type and one default value is therir called file name

if len(sys.argv) ==1:
  print("USAGE: Python3 app.py <passowrd>")
else:
  password = sys.argv[1]
  print("Password",password)  