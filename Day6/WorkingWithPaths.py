from pathlib import Path

# Path("/user/local/bin") #absolute path
# Path()
# Path("./PythonStandardLibrary.py") #relative path
# Path() /"foldername"/"filename.py"
# Path.home() #it return home directory
#  mainly used this type

path = Path("./PythonStandardLibrary.py") #relative path
path.exists()
path.is_file()
path.is_dir()

print(path.name) #with extension
print(path.stem) #without extension
print(path.suffix) #extension only
print(path.parent) #parent folder name

path = path.with_name("file.txt") # it does not exist but we can create paths
print(path.absolute)
path = path.with_suffix(".txt")  # to cahnge prensent file extension we can use this one
print(path)