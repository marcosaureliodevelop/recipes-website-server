from flask import Flask
from .extensions import db, migrate
from .routes import register_routes
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)

    return app
