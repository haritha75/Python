import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()


# with sqlite3.connect("db.sqlite3") as conn:
#     command = "select * from Movies"
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)
        
with sqlite3.connect("db.sqlite3") as conn:
    command = "select * from Movies"
    cursor = conn.execute(command)
    movies = cursor.fetchall() # we are fetch all the data at a time
    print(movies)
   
      