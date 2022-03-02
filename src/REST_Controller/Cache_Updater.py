from src.Store.Cache import CACHE_STORE
from Database.Database_Interaction import getLibrariesFromDatabase
from Middlewares.Middlewares import lock, timer
import time

def performUpdate():
    if lock.status() == 0:
        libraries_from_database = getLibrariesFromDatabase()
        CACHE_STORE.updateCache(libraries_from_database)
        timer.setCacheUpdateTime(time.time())    

def updateCache():
    time_lapse = time.time() - timer.getCacheUpdateTime()
    if time_lapse >= 5 or timer.getCacheUpdateTime() == 0:
        performUpdate()
    else:
        time.sleep(5 - time_lapse)
        performUpdate()

