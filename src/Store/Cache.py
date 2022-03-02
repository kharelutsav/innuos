class Cache:

    def __init__(self) -> None:
        self.__cache = {}

    # def __new__(cls):
    #     if not hasattr (cls, "instance"):
    #         cls.instance = super(Cache, cls).__new__(cls)
    #     return cls.instance

    def getCacheCount(self):
        return len(self.__cache)

    def getCache(self):
        return self.__cache
    
    def updateCache(self, jsonObj: dict):
        self.__cache.update(jsonObj)

CACHE_STORE = Cache()
