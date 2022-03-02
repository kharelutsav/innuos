from src.Store.Cache import CACHE_STORE
from REST_Controller.Database_Interaction import getLibrariesFromDatabase


def updatesCache():
    libraries_from_database = getLibrariesFromDatabase()
    CACHE_STORE.updateCache(libraries_from_database)

