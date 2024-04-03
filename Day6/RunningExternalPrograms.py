import subprocess

subprocess.run(['ls']) # it gives all files list
subprocess.run(["ls","-l"]) # more info about the file

res = subprocess.run(["ls","-l"], capture_output=True,text=True) # making true here we canot see all the files here only to print stdout then we can see otherwise not
print(type(res))

print("args",res.args)
print("returncode",res.returncode)
print("stderr",res.stderr)
print("stdout",res.stdout)


res = subprocess.run(["python3","other.py"], capture_output=True,text=True) # making true here we canot see all the files here only to print stdout then we can see otherwise not
print("args",res.args)
print("returncode",res.returncode) # if return code 0 then it succesfukll excuted if 1 not excuted successfully
print("stderr",res.stderr)
print("stdout",res.stdout)


res = subprocess.run(["False"], capture_output=True,text=True,check=True) # making true here we canot see all the files here only to print stdout then we can see otherwise not
# here check if is their any error it risies the exception
print("args",res.args)
print("returncode",res.returncode) # if return code 0 then it succesfukll excuted if 1 not excuted successfully
print("stderr",res.stderr)
print("stdout",res.stdout)

if res.returncode!=0:
  print(res.stderr)


# another way
  
try:
    res = subprocess.run(["False"], capture_output=True,text=True,check=True) # making true here we canot see all the files here only to print stdout then we can see otherwise not
    print("args",res.args)
    print("returncode",res.returncode) # if return code 0 then it succesfukll excuted if 1 not excuted successfully
    print("stderr",res.stderr)
    print("stdout",res.stdout)
except subprocess.CalledProcessError as er:
   print(er)