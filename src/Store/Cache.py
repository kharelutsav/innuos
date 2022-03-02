class Cache(object):

    def __init__(self) -> None:
        self.__cache = {}

    def getCacheCount(self):
        return len(self.__cache)

    def getCache(self):
        return self.__cache
    
    def updateCache(self, jsonObj: dict):
        self.__cache.update(jsonObj)

CACHE_STORE = Cache()
