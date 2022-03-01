from UI_Receiver import sio, app
import socketio

if __name__ == "__main__":
    application = socketio.WSGIApp(sio, app)
