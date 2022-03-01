class extraStuff:
    def __init__(self) -> None:
        self.__last_updated = 0 
        self.lock_status = 0     

    def setCacheUpdateTime(self, updated_time):
        self.__last_updated = updated_time

    def getCacheUpdateTime(self):
        return self.__last_updated

    def setLockStatus(self, status):
        self.lock_status = status
