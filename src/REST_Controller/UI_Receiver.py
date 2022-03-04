import socketio
import json
from src.REST_Controller.server import sio, app
from flask import Response, jsonify, request
from REST_Controller.Cache_Updater import updateCache
from src.Store.Cache import CACHE_STORE
from decouple import config
from os import path
from Middlewares.Middlewares import lock
from Database.Database_Interaction import addPlaylist, addMusic



if CACHE_STORE.getCacheCount() == 0:
    updateCache()


@app.route("/library", methods=["GET"]) ############### COMPLETED FOR NOW
@app.route("/", methods=["GET"])
def getLibrary():
    try:
        data = CACHE_STORE.getPlaylists()
        return jsonify(data)
    except FileNotFoundError:
        return Response("Resource Not Found", 404, mimetype = "text/html")


@app.route("/library/<playlist>", methods=["GET"]) ############### COMPLETED FOR NOW
def getPlaylist(playlist):
    try:
        data = CACHE_STORE.getPlaylist(playlist)
        return jsonify(data)
    except:
        return Response("Playlist Unavailable", 404, mimetype = "text/html")


@app.route("/library/<playlist>/<song>", methods=["GET"]) ############### COMPLETED FOR NOW
def streamMusic(playlist, song): 
    try:
        def generator():
            with open(f"music\{song}.mp3", "rb") as read_music:
                music = read_music.read(1024)
                while music:
                    yield music
                    music = read_music.read(1024)
        return Response(generator(), mimetype="audio/mp3")
    except:
        return Response("Playlist Unavailable", 404, mimetype = "text/html")


@app.route("/upload/<Songname>", methods=["POST"]) ########## FUNCTION TO HANDLE UPLOAD $$$$$$ VALIDATION $$$$$$
def saveMusicFile(Songname):
    music = request.files["file"]
    music.save(path.join(config("UPLOAD_FOLDER"),Songname))
    return Response(status=200)

@app.route("/addplaylist/<playlist>", methods=["POST"]) ######### PLAYLIST ADD METHOD IMPLEMENTED $$$$$ OPTIMIZE $$$$$
def addPlaylistToLibrary(playlist):
    try:
        addPlaylist(playlist)
        updateCache()
        return Response(f"{playlist} added to the library.", 200, mimetype="text/html")
    except:
        return Response("Playlist already exists in the Library.", 403, mimetype = "text/html")

@app.route("/addmusic/<music>", methods=["POST"]) ######### MUSIC ADD METHOD IMPLEMENTED $$$$$ OPTIMIZE $$$$$
def addMusicToLibrary(music):
    try:
        addMusic(music, "test/path/2", "default/path")
        updateCache()
        return Response(f"{music} added to the library.", 200, mimetype="text/html")
    except:
        return Response("Music already exists in the Library.", 403, mimetype = "text/html")


# @app.route("/update", methods=["POST"])
# def receiveUpdatesFrom_UI_Receiver():
#     try:
#         with open("src\Store\Database.json", "r+") as read_json_file:
#             old_library = json.load(read_json_file)
#             old_library.update(request.json)
#             read_json_file.seek(0)
#             json.dump(old_library, read_json_file, indent=4)
#         return jsonify(old_library)
#     except TypeError:
#         return Response("Unable to submit form data.", 403, mimetype = "text/html")
#     except RuntimeError:
#         return Response("Unable to submit form data.", 403, mimetype = "text/html")


@app.errorhandler(404)
def pageNotFound(e):
    return Response("The path you requested does not exist.", 404, mimetype = "text/html")


application = socketio.WSGIApp(sio, app)
