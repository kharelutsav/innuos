import socketio
import json
from src.REST_Controller.server import sio, app
from flask import Response, jsonify, request
from REST_Controller.Cache_Updater import updatesCache
from src.Store.Cache import CACHE_STORE

@app.route("/", methods=["GET"])
def getLibrary():
    try:
        if CACHE_STORE.getCache() != []:
            data = CACHE_STORE.getCache()
        else:
            updatesCache()
            data = CACHE_STORE.getCache()
        return jsonify(data)
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
        with open("src\Store\Database.json", "r+") as read_json_file:
            old_library = json.load(read_json_file)
            old_library.update(request.json)
            read_json_file.seek(0)
            json.dump(old_library, read_json_file, indent=4)
        return jsonify(old_library)
    except TypeError:
        return Response("Unable to submit form data.", 403, mimetype = "text/html")
    except RuntimeError:
        return Response("Unable to submit form data.", 403, mimetype = "text/html")


application = socketio.WSGIApp(sio, app)
