from REST_Controller.main import sio, app
from flask import Response
import socketio
from Middlewares.Middlewares import *


@app.route("/", methods=["GET"])
def getLibrary(request):
    return Response("Hello, World!", 200, mimetype = "text/html")

@app.route("/", methods=["POST",])
def receiveUpdatesFrom_UI_Receiver(request):
    return Response("Update Completed!", 200, mimetype = "text/html")


application = socketio.WSGIApp(sio, app)
