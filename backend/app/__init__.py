from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, migrate
from flask_cors import CORS 
from flask_socketio import SocketIO
from .database import Session
from .database import Base
from .database import engine


login_manager = LoginManager()
migrate = Migrate()
socket_io = SocketIO()
db = Session()

def create_app():

    app = Flask(__name__)

    Base.metadata.create_all(engine)

    @app.teardown_appcontext
    def remove_session(*args, **kwargs):
        db.remove()
