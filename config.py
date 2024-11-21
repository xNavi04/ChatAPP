from flask import Flask
from flask_bootstrap import Bootstrap5
from models import db
import os
from flask_login import LoginManager
from flask_socketio import SocketIO

endpoint_secret = "whsec_98a1720fbee9038c2393b8e5a42b861476f232f6f1eb1a31f1a5b1a100449f3d"#os.environ.get("ENDPOINT_SECRET")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", endpoint_secret)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
    db.init_app(app)
    Bootstrap5(app)
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    socketio = SocketIO()
    socketio.init_app(app, cors_allowed_origins="*")

    with app.app_context():
        db.create_all()

    return app, login_manager, socketio, db
