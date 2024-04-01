def getGreeting(name):
  return f"Hi {name}"

message = getGreeting("Haritha")
print(message)
file = open("Greeting.txt", "w") 
file.write(message)
