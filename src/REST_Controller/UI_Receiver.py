from flask import Flask
from socketio import Server
from decouple import config


sio = Server(cors_allowed_origin="*", async_handlers=True, async_mode=None)

app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')

