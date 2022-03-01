import socketio
from REST_Controller.server import sio, app
from flask import Response, jsonify, request
from Middlewares.Middlewares import *


@app.route("/", methods=["GET"])
def getLibrary():
    try:
        with open("src\Data.json", "r") as data:
            data = data.readlines()
            sio.emit("Gotcha")
        return Response(data, 200, mimetype = "application/json")
    except FileNotFoundError:
        return Response("Resource Not Found", 404, mimetype = "text/html")


@app.route("/update", methods=["POST"])
def receiveUpdatesFrom_UI_Receiver():
    try:
        return request.json
    except TypeError:
        return Response("Unable to submit form data.", 403, mimetype = "text/html")
    except RuntimeError:
        return Response("Unable to submit form data.", 403, mimetype = "text/html")


application = socketio.WSGIApp(sio, app)
