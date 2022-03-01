# Linearize writes to the database:
class Lock:
    def __init__(self):
        self.__blocked = 0
    
    def block(self):
        self.__blocked = 1
        # sio.emit('status update', {'data': f'{self.__blocked}'})

    def release(self):
        self.__blocked = 0
        # sio.emit('status update', {'data': f'{self.__blocked}'})

    def status(self):
        return self.__blocked

lock = Lock()

def linearise():
    pass

def synchronise():
    pass

def cacheTimers():
    pass