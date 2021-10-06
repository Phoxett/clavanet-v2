from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_marshmallow import Marshmallow
import os

resources = {
    r"/teacher/login": {},
    r"/teacher/logout": {},
    r"/teacher/signup": {},
    r"/student/login": {},
    r"/student/logout": {},
    r"/student/signup": {},
}

db = SQLAlchemy()
cors = CORS(
    resources,
    origins=["http://localhost:8000", "https://school.phoxett.com"],
    methods= ["GET", "POST", "PUT", "DELETE"],
    supports_credentials=True
)
api = Api()
jwtmanager = JWTManager()
mail = Mail()
socketio = SocketIO()
marshmallow = Marshmallow()

def create_app():

    app = Flask(__name__)

    DB_URL = os.getenv("DB_URL")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    app.config['SQLALCHEMY_DATABASE_URL'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_URL}/{DB_NAME}'
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['MAIL_SERVER'] = MAIL_SERVER
    app.config['MAIL_PORT'] = MAIL_PORT
    app.config['MAIL_USERNAME'] = MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)
    jwtmanager.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)
    marshmallow.init_app(app)


    with app.app_context():

        from .teacher import teacher

        app.register_blueprint(teacher.teacherbp)

        db.create_all()
        return app
