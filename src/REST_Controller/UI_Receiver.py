from flask import make_response
from REST_Controller.main import sio, app
from flask import make_response
import socketio

@app.route("/", methods=["GET"])
def getLibrary():
    response = make_response("Hello, World!", 200)
    response.mimetype = "text/html"
    return response

@app.route("/", methods=["POST",])
def updateRequestFromUI_Receiver(request):
    return "Hello, World!"

application = socketio.WSGIApp(sio, app)
