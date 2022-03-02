# from DatabaseConnection import con
from Database.DatabaseConnection import con

cur = con.cursor()

def getOnlyLibrariesFromDatabase():
    data = []
    query = "SELECT library_name FROM Library"
    cur.execute(query)
    for (lib,) in cur:
        data.append(lib)
    return data

def getMusicsFromDatabase(library_name):
    query = ("SELECT music_name FROM collection WHERE library_name = %s")
    params = library_name
    cur.execute(query, params)
    collections = cur.fetchall()
    return collections    

def getLibrariesFromDatabase():
    buffer = {}
    query = "SELECT library.library_name, music.music_name, music.music_file, music.thumbnail_image\
        FROM library LEFT JOIN collection on\
        library.library_name = collection.library_name\
        RIGHT JOIN music on\
        collection.music_name = music.music_name;"
    cur.execute(query)
    for (library_name, music_name, file_path, image_path) in cur:
        if not library_name in buffer:
            buffer[library_name] = [[music_name, file_path, image_path]]
            continue
        buffer[library_name].append([music_name, file_path, image_path])
    return buffer
