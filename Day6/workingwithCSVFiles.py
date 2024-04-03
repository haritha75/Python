# comma seperated file
import csv
# write mode
# with open("data.csv","w") as file:
#   writer =  csv.writer(file)
#   writer.writerow(["id","name","age"])
#   writer.writerow([100,"Haritha",22])


# read mode
  
with open("data.csv") as file:
  reader =  csv.reader(file)
  print(list(reader))

# in csv files data will be list of list
  
with open("data.csv") as file:
  reader =  csv.reader(file)
  for row in reader:
    print(row)
