from pathlib import Path

path = Path("./ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecom")

print(path.iterdir()) # it returns generator object we cannot get values directly so then use iterator
for i in path.iterdir():
  print(i)

# list comprehension
  paths = [p for p in path.iterdir() if p.is_dir()]
  print(paths)

py = [p for p in path.glob("*.py")] #only .py files
print(py)
py = [p for p in path.glob("*.*")] # all fikes
print(py)

py = [p for p in path.rglob("*.py")] # all files in this folder
print(py)
