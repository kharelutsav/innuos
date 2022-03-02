from src.Store.Cache import CACHE_STORE
from REST_Controller.Middlewares import fetchDataFromDatabase
from REST_Controller.server import sio


def updateCache():
    library_from_database = fetchDataFromDatabase()
    CACHE_STORE.updateCache(library_from_database)

@sio.event
def connect():
    print("Connected to the server.", sio.sid)

