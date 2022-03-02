from src.Store.Cache import CACHE_STORE
from src.Middlewares.Middlewares import fetchDataFromDatabase
from server import sio


def updateCache():
    library_from_database = fetchDataFromDatabase()
    CACHE_STORE.updateCache(library_from_database)

@sio.event
def connect():
    print("Connected to the server.", sio.sid)

@sio.on("Update Cache")
def update():
    updateCache()

