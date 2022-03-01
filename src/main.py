import eventlet
from eventlet import wsgi
from src.REST_Controller.UI_Receiver import application


if __name__ == "__main__":
    wsgi.server(eventlet.listen(("", 3000)), application)
