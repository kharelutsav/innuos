# from DatabaseConnection import con
from REST_Controller.DatabaseConnection import con

cur = con.cursor()

def getLibrariesFromDatabase():
    data = []
    query = "SELECT library_name FROM Library"
    cur.execute(query)
    for (lib,) in cur:
        data.append(lib)
    return data

def GetMusicsFromDatabase(library_name):
    query = ("SELECT music_name FROM collection WHERE library_name = %s")
    params = library_name
    cur.execute(query, params)
    collections = cur.fetchall()
    return collections

# for i in range(len(count)):
#     GetMusicsFromDatabase(count[i])
