point = {"x":1,"2":"Haritha",3.4:11}
point = dict([("x", 1), ("haritha", 22)])
point = dict(a=1,b=2.2)
print(point)
point['a']=123
print(point)
point = dict.fromkeys([1,2,3,4],0)
print(point)
# using key get value
print(point[1])
print(point.get(1))
point.pop(1)
print(point)
del point[2]
print(point)
if 3 in point:
  print("YES")

print(point.keys()) 
print(point.values())  
print(point.items())  
point.clear()
print(point)

point = {"x":1,"2":"Haritha",3.4:11}

for key,values in point.items():
  print(key,values)
