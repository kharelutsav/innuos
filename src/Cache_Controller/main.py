from Cache_Updater import sio

if __name__ == "__main__":
    sio.connect("http://localhost:3000")
    sio.wait()