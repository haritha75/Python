# javascript object notations
import json
from pathlib import Path
movies = [
  {"id":1,"title":"terminator","year":1989},
  {"id":3,"title":"Hrudayam","year":1999}

]

data  = json.dumps(movies) #converting that data into json format
# print(data)

Path("movies.json").write_text(data) #writting that data in to another json file

# read the  json data from file

data = Path("movies.json").read_text()
print(data)
movies = json.loads(data)
print(movies[0])
print(movies[0]["title"])