class Cache:

    def __init__(self) -> None:
        self.__library_cache = []
        self.__playlists_cache = []

    def getCacheCount(self):
        return len(self.__playlists_cache)

    def getLibrary(self):
        return len(self.__library_cache)

    def getPlaylists(self):
        return self.__playlists_cache

    def getPlaylist(self, playlist):
        return self.__library_cache[playlist]
    
    def updateLibraryCache(self, jsonObj):
        self.__library_cache = jsonObj

    def updatePlaylistsCache(self, jsonObj):
        self.__playlists_cache = jsonObj

CACHE_STORE = Cache()
