# from DatabaseConnection import con
from Database.DatabaseConnection import con

cur = con.cursor()

def getLibrariesFromDatabase():
    library = {}
    playlists = []
    query = ("SELECT library.library_name, music.music_name, music.music_file, music.thumbnail_image\
        FROM library LEFT JOIN collection on\
        library.library_name = collection.library_name\
        RIGHT JOIN music on\
        collection.music_name = music.music_name;")
    cur.execute(query)
    for (library_name, music_name, file_path, image_path) in cur:
        if not library_name in playlists:
            playlists.append(library_name)
            library[library_name] = [[music_name, file_path, image_path]]
            continue
        library[library_name].append([music_name, file_path, image_path])
    if None in playlists:
        playlists.remove(None)
        playlists.append("Unclassified")
        library["Unclassified"] = library.pop(None)
    return playlists, library


def addPlaylist(playlist):
    query = ("INSERT INTO Library(library_name) VALUES (%s)")
    values = [playlist,]
    cur.execute(query, values)
    con.commit()


def addMusic(music_name, file_path, image_path):
    query = ("INSERT INTO Music(music_name, music_file, thumbnail_image) VALUES (%s, %s, %s)")
    values = (music_name, file_path, image_path)
    cur.execute(query, values)
    con.commit()


def addMusicToPlaylist(playlist, ):
    pass

