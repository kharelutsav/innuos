from distutils.log import error
from os import path, getcwd
from REST_Controller.main import sio, app
from flask import Response
import socketio
from Middlewares.Middlewares import *


@app.route("/", methods=["GET"])
def getLibrary():
    try:
        with open("src\Data.json", "r") as data:
            data = data.readlines()
        return Response(data, 200, mimetype = "application/json")
    except FileNotFoundError:
        return Response("Test Failed!", 200, mimetype = "text/html")


@app.route("/", methods=["POST",])
def receiveUpdatesFrom_UI_Receiver():
    return Response("Update Completed!", 200, mimetype = "text/html")


application = socketio.WSGIApp(sio, app)
