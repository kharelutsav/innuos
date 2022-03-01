import socketio
import json
from REST_Controller.server import sio, app
from flask import Response, jsonify, request


@app.route("/", methods=["GET"])
def getLibrary():
    try:
        with open("src\Data.json", "r") as data:
            data = data.readlines()
            sio.emit("Gotcha")
        return Response(data, 200, mimetype = "application/json")
    except FileNotFoundError:
        return Response("Resource Not Found", 404, mimetype = "text/html")

@app.route("/<library>/<song>", methods=["GET"])
def streamMusic(library, song):
    def generator():
        with open(f"music\{library}\{song}.mp3", "rb") as my_music:
            music = my_music.read(1024)
            while music:
                yield music
                music = my_music.read(1024)
    return Response(generator(), mimetype="audio/mp3")   

@app.route("/update", methods=["POST"])
def receiveUpdatesFrom_UI_Receiver():
    try:
        with open("src\Data.json", "r") as read_database:
            old_library = json.load(read_database)
        old_library.update(request.json)
        with open("src\Data.json", "w") as write_database:
            write_database.write(json.dumps(old_library, indent=4))
        return jsonify(old_library)
    except TypeError:
        return Response("Unable to submit form data.", 403, mimetype = "text/html")
    except RuntimeError:
        return Response("Unable to submit form data.", 403, mimetype = "text/html")


application = socketio.WSGIApp(sio, app)
