from flask import Flask
from app.config import Config
from app.extensions import db
from app.routes.plate_recognizer import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        init_routes(app)

    return app 