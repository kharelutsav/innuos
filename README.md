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
1   Many smaller queries though increases overhead, helps reduce the unnecessary 
    database queries. But, due to insufficient knowledge on requirements, large
    queries are used for updating in-memory cache (No cache libraries used.).
    Could be modified if required.

2   Database: 1
    Tables: 3
        library:
            library_name (Primary Key)
        music:
            music_name (Primary Key)
            music_file (Relative path to the image file.)  (Not null)
            thumbnail_image (Relative path to the image file.) (Null allowed)
        collection:
            library_name (Foreign Key) (Indexed)
            music_name (Foreign Key) (Indexed)

