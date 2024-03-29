i=1
while i<10:
  if(i==5):
    break
  print(i)
  i=i+1
else:
  print("This will be printed only once")  

#  difference is when break statement comes we cannot print else block because we are comming out of loop but not come to else block also but in normal form we can print
for i in range(10):
  if(i==5):
    break
  print(i)
print("this will be printed only once")  

# with out break after completing the loop else block na dnormal block executed but if you use break in normal will be executed but not else  else block will be executed when loop will be finished on that time only executed


# use like this also

n = int(input())

for i in range(2,n,1):
  if n%i==0:
    break
else:
  print("Prime")  

  