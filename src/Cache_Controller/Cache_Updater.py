from flask import Flask
import socketio
from decouple import config


sio = socketio.Server(cors_allowed_origin="*", async_handlers=True, async_mode=None)

app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')

