class Timer:
    """
    Keeps control on how frequently can cache be updated.
    """
    def __init__(self) -> None:
        self.__last_updated = 0

    def setCacheUpdateTime(self, updated_time: int) -> None:
        self.__last_updated = updated_time

    def getCacheUpdateTime(self) -> int:
        return self.__last_updated

class Lock:
    """
    Stops the cache update if write is hapenning to the database.
    """
    def __init__(self) -> None:
        self.__blocked = 0
    
    def block(self) -> None:
        self.__blocked = 1

    def release(self) -> None:
        self.__blocked = 0

    def status(self) -> int:
        return self.__blocked


timer = Timer()
lock = Lock()
