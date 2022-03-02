import collections
from DatabaseConnection import con

cur = con.cursor()

def GetLibrariesFromDatabase():
    query = "SELECT library_name FROM Library"
    cur.execute(query)
    data = cur.fetchall()
    return data
count = GetLibrariesFromDatabase()

def GetMusicsFromDatabase(library_name):
    query = ("SELECT music_name FROM collection WHERE library_name = %s")
    params = library_name
    cur.execute(query, params)
    collections = cur.fetchall()
    print(collections)

for i in range(len(count)):
    GetMusicsFromDatabase(count[i])
