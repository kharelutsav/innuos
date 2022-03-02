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
    database queries. Hence, is selected approach for updating cache.

2   

