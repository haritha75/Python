from pathlib import Path
from zipfile import ZipFile
with ZipFile("files.zip","w") as zip: # create file
  for path in Path("./ecommerce").rglob("*.*"): # whatever the files in this folder we are writting all the data in this zip file
    zip.write(path)

with ZipFile("files.zip") as zip:
  print(zip.namelist())
  # info = zip.getinfo("./ecommerce/pac1/Hello1.py") 
  # print(info.compress_size)
  # print(info.file_size)
  zip.extractall("extract") # here whatever files in size zip we are extracting and putting into one folder that folder willl be created