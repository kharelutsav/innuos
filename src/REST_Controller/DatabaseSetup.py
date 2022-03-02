from DatabaseConnection import con

cursor = con.cursor()
query = "CREATE TABLE IF NOT EXISTS Library(\
    library_name VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE);"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS Music(\
    music_name VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE,\
    music_file CHAR(140) NOT NULL UNIQUE,\
    thumbnail_image CHAR(140)\
    );"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS Collection(\
    library_name VARCHAR(200),\
    music_name VARCHAR(200),\
    INDEX(library_name),\
    INDEX(music_name),\
    FOREIGN KEY (library_name) REFERENCES Library(library_name),\
    FOREIGN KEY (music_name) REFERENCES Music(music_name)\
    );"
cursor.execute(query)

