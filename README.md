# innuos
Clone Repository: git clone https://github.com/kharelutsav/innuos.git

# Create Virtual Environment
    python -m venv innuos
    cd innuos && .\Scripts\activate
    
    Start Point: main.py

# Libraries Used:
    flask (python web frame-work)
    Visit: https://flask.palletsprojects.com/en/2.0.x/
    Installation: pip install flask

    python-socketio (python socketio library)
    Visit: https://python-socketio.readthedocs.io/en/latest/
    Installation: pip install python-socketio && pip install "python-socketio[client]"

    eventlet (concurrent networking library)
    Visit: https://eventlet.net/doc/
    Installation: pip install eventlet

    python-decouple (Library for accessing .env variables)
    Visit: https://pypi.org/project/python-decouple/
    Installation: pip install python-decouple

    MySQL Connector/Python
    Visit: https://dev.mysql.com/doc/connector-python/en/
    Installation: pip install mysql-connector-python

# Decisions:
1   Singleton Design Pattern with Object Oriented Programming approach

2   Many smaller queries though increases overhead, helps reduce the unnecessary 
    database queries. But, due to insufficient knowledge on requirements, large
    queries are used for updating in-memory cache (No cache libraries used.).
    Could be modified if required.

3   Database: 1
    Tables: 3
        1   library:
                library_name (Primary Key)
        2   music:
                music_name (Primary Key)
                music_file (Relative path to the image file.)  (Not null)
                thumbnail_image (Relative path to the image file.) (Null allowed)
        3   collection:
                library_name (Foreign Key) (Indexed)
                music_name (Foreign Key) (Indexed)

# TODO: Work on upload function
The update function should be able to receive updates on music library.
Create playlist to create and manage playlists.
Create endpoints to get and update playlists.
Update cache class to classify libraries and playlists.
This much for tomorrow.

# Completed: 
    Table(Music) A.K.A. Library
    Table(Library) A.K.A. Playlists
    Created in-memory cache and functions to populate it

