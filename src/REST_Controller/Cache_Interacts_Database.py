from DatabaseConnection import con

cur = con.cursor()

def GetLibrariesFromDatabase():
    query = "SELECT library_name FROM Library"
    libraries = cur.execute(query)

def GetMusicsFromDatabase(library):
    query = "SELECT * FROM Music WHERE "
