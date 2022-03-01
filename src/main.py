import eventlet
from eventlet import wsgi
from REST_Controller.main import application


if __name__ == "__main__":
    wsgi.server(eventlet.listen(('', 3000)), application)