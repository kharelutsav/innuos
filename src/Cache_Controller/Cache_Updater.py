from socketio import Client


sio = Client()

@sio.event
def connect():
    print("Connected to the server.", sio.sid)

@sio.event
def Gotcha():
    print("Yay working!")

